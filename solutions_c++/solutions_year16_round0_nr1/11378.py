#include<bits/stdc++.h>
using namespace std;
int main()
{//
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t; scanf("%d",&t);
	int N=t;
	while(t--)
	{
		int n; scanf("%d",&n);
		int cnt=0;
		vector<int> c(10,0);
		if(n==0) { printf("Case #%d: INSOMNIA\n",N-t); continue; }
		int tmp=0,cur=0;
		int b=0;
		while(!b)
		{
			cur+=n;
			tmp=cur;
			//cnt=0;
			while(tmp > 0)
			{
				int id=tmp%10;
				if(c[id]==0) 
					++cnt;
				if(cnt==10) b=1;
				c[id]=1;
				tmp/=10;
			}
		}
		printf("Case #%d: %d\n",N-t,cur);
	}
	return 0;
}