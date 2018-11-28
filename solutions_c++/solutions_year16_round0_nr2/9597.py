#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

int solve(string s)
{
	int cur = 1, res = 0;

	reverse(s.begin(), s.end());

	for (int i = 0; i < s.size(); i++)
	{
		if ((s[i] == '+' && cur == 0) || (s[i] == '-' && cur == 1))
		{
			cur = (cur + 1) % 2;
			res++;
		}
	}	

	return res;
}

int main()
{
	string s;	
	int t;
	cin >> t;
	getline(cin, s);

	for (int i = 1; i <= t; i++)
	{
		string s;
		getline(cin, s);
		printf("Case #%d: %d\n", i, solve(s));
	}	

	return 0;
}
