#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

const int maxn = 11;
int n,f[11],p[11];

int main()
{
	//freopen("test.txt","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("ansC.txt","w",stdout);
	int  T;
	scanf("%d",&T);
	for(int z=1;z<=T;++z)
	{
		scanf("%d",&n);
		for(int i=0;i<n;++i) scanf("%d",f+i+1);
		int ans = 0;
		for(int i=0;i<n;++i) p[i] = i+1;
		do
		{
			int res = 0;
			for(int i=1;i<n;++i)
			{
				if((f[p[i]] == p[i-1] || f[p[i]] == p[0]) && (f[p[0]] == p[1] || f[p[0]] == p[i]))
				{
					res = i+1;
				}
				if(f[p[i]] != p[i-1] && (i != n-1 && f[p[i]] != p[i+1])) break;
			}
			//printf("..%d\n",res);
			//for(int i=0;i<n;++i) printf("%d ",p[i]);
			ans = max(res,ans);
		}while(next_permutation(p,p+n));
		printf("Case #%d: %d\n",z,ans);	
	}
	return 0;
}
