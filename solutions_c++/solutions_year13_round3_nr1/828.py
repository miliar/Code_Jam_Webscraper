#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

bool vowel(char c)
{
	return (c == 'a' || c == 'e' || c == 'i' ||
		    c == 'o' || c == 'u');
}

long long Gum(long long n)
{
	return n*(n+1)/2;
}

long long SqGum(long long n)
{
	return n*(n+1)*(2*n+1)/6;
}

long long Count(long long i, long long a, long long n, long long L)
{
	long long T = L - i - n + 2;
	long long answer = (i+1)*(L - i - n + 1);
	answer += (a - n)*(L - i - n + 1);
	answer -= Gum(a - n);
	//cout << i << " " << a << " " << n << " " <<  L << "  =  " << answer << endl;
	return answer;
}

long long solve(const string& s, long long n)
{
	long long a = 0, start = -1, answer = 0;
	long long toxEnd = 0;
	for (long long i = 0; i < s.size(); ++i)
		if (!vowel(s[i]))
		{
			if (start == -1)
			{
				start = i;
				a = 1;
			}
			else
				++a;
		}
		else
		{
			if (a >= n)
			{
				answer += Count(start - toxEnd, a, n, s.size() - toxEnd);
				toxEnd = start + a - n + 1;
				//cout << toxEnd << endl;
			}
			a = 0;
			start = -1;
		}
	if (start != -1 && a >= n)
		answer += Count(start - toxEnd, a, n, s.size() - toxEnd);
	return answer;
}

int main()
{
	int test, t, n;
	string s;

	in >> test;
	
	for (t = 1; t <= test; ++t)
	{
		in >> s >> n;

		long long ans = solve(s, n);

		out << "Case #" << t << ": " << ans << endl;		
	}

	return 0;
}