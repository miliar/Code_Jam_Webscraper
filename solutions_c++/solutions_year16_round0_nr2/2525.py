#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <iomanip>
#pragma comment(linker, "/STACK:200000000")
using namespace std;
bool digits[10];
bool check()
{
	bool ok = true;
	for (int i = 0; i < 10; ++i)
		if (!digits[i])
			ok = false;
	return ok;
}
void getdigits(long long n)
{
	while (n > 0ll)
	{
		digits[n % (10ll)] = true;
		n /= 10ll;
	}
}
int main()
{
	ifstream in("B-large.in");
	ofstream out("small.out");
	int tests;
	string word;
	int len;
	char last = '?';
	char first;
	in >> tests >> ws;
	for (int t = 1; t <= tests; ++t)
	{
		in >> word;
		len = 1;
		last = word[0];
		first = last;
		for (int i = 1; i < word.length(); ++i)
		{
			if (word[i] != last)
			{
				last = word[i];
				len++;
			}
		}
		if (last == '+')
			len -= 1;
		int ans;
		len/=2;
		if (first == '-')
		{
			ans = 2 * len + 1;
		}
		else
			ans = 2 * len;
		out << "Case #" << t << ": " << ans << endl;
		
	}

	//system("pause");
	in.close();
	out.close();
	return 0;
}