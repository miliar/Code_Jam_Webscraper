#include<iostream>
#include<algorithm>
#include<functional>
#include<cstdio>
#include<string>
#include<stdio.h>
#define ll long long
using namespace std;
FILE *stream;

int main()
{

	freopen_s(&stream,"R:\\in.in", "r", stdin);
	freopen_s(&stream,"R:\\out.txt", "w", stdout);
	int t,T,n,i,temp;
	string s;
	cin >> T;
	for (t = 1; t <= T;++t)
	{
		cin >> n;
		cin >> s;
		int cnt = s[0]-'0',ans=0;
		for (i = 1; i < s.size(); ++i)
		{
			temp = s[i] - '0';
			if (i > cnt)
			{
				ans += i - cnt;
				cnt = i;
			}
			cnt += temp;
		}
		cout << "Case #"<< t <<": "<<ans << endl;

	}
	return 0;
}