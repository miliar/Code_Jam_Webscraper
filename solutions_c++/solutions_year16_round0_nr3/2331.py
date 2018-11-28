#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;

bool isPrime(long long n, long long& x)
{
	bool flag = true;
	if (n == 1)
	{
		return (false);
	}
	for (long long i = 2; i*i <= n; i++) 
	{
		if (n % i == 0) 
		{
			flag = false;
			x = i;
			break;
		}
	}
	return flag;
}

class Radix {
private:
	const char* s;
	int a[128];
public:
	Radix(const char* s = "0123456789ABCDEF") : s(s) {
		int i;
		for (i = 0; s[i]; ++i)
			a[(int)s[i]] = i;
	}
	std::string to(long long p, int q) {
		int i;
		if (!p)
			return "0";
		char t[64] = {};
		for (i = 62; p; --i) {
			t[i] = s[p % q];
			p /= q;
		}
		return std::string(t + i + 1);
	}
	std::string to(const std::string& t, int p, int q) {
		return to(to(t, p), q);
	}
	long long to(const std::string& t, int p) {
		int i;
		long long sm = a[(int)t[0]];
		for (i = 1; i < (int)t.length(); ++i)
			sm = sm * p + a[(int)t[i]];
		return sm;
	}
};

string generateString(long long i, int N, bool& b)
{
	Radix r;
	string tmp = r.to(i, 2);
	int size = tmp.size();
	if (size == N && tmp[0] == '1' && tmp[size - 1] == '1')
	{
		b = true;
	}

	return (tmp);
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;
    for (int j = 0; j < T; j++)
    {
		fout << "Case #" << j + 1 << ":" << endl;
	
		int N;
        fin >> N;
		int J;
		fin >> J;

		long long x[9];
		int count = 0;
		for (long long i = 0; count != J; i++)
		{
			bool bb = false;
			string a = generateString(i, N, bb);
			if (bb == false)
			{
				continue;
			}
			bool flag = false;
			for (int i = 2; i <= 10; i++)
			{
				Radix r;
				string b = r.to(a, i, 10);
				if (isPrime(stoll(b), x[i - 2]) == true)
				{
					flag = true;
					break;
				}
			}
			if (flag == false)
			{
				fout << a;
				for (int i = 0; i < 9; i++)
				{
					fout << " " << x[i];
				}
				fout << endl;
				count++;
			}
		}
    }
	
    return (0);
}
