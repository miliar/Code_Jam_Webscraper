#include<bits/stdc++.h>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)
#define foreach(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, t = 0;
	scanf("%d", &T);
	while(T--)
	{
		t++;
		long long x, ox;
		scanf("%lld", &x), ox = x;
		int mask = 0;
		if(x == 0) printf("Case #%d: INSOMNIA\n", t);
		else
		{
			while(true)
			{
				long long y = x;
				while(y)
				{
					mask |= 1<<(y%10);
					y/=10;
				}
				if(mask == (1<<10)-1) break;
				x += ox;
			}
			printf("Case #%d: %d\n", t, x);
		}
	}
    
}






