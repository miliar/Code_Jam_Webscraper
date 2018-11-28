/*
https://code.google.com/codejam/contest/6254486/dashboard#s=p0
*/

#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int vis[10];
int main()
{
	int tc;
	cin >> tc;
	for(int cases=1;cases<=tc;cases++)
	{
		long long st,t;
		memset(vis,0,sizeof(vis));
		cin >> st;
		if(0==st) cout << "Case #" << cases << ": INSOMNIA\n";
		else
		{
			for(int i=1;;i++)
			{
				t   = st*i;
				while(t)
				{
					vis[t%10] 	= 1;
					t		 	= t/10;
				}
				int j = 0;
				for(j=0;j<=9;j++)
				{
					if(vis[j]==0) break;
				}
				if(10==j) 
				{
					cout << "Case #" << cases << ": " << st*i << endl;
					break;
				}
			}
		}
	}
	return 0;
}
