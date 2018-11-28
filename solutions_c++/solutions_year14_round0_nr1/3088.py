#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define ll long long 
#define bug puts("here");
#define maxn 20000
#define mm 1000000007
int v[5][5];
int cnt;
int ans[10];
using namespace std;
int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\A-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\新建文本文档.txt","w",stdout);
	int T,n,m,cas=1;
	cin>>T;
	while(T--)
	{
		cnt=0;
		for(int kase=0;kase<2;++kase)
		{
		scanf("%d",&n);
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
			{
				scanf("%d",&v[i][j]);
				if(i==n)
					ans[cnt++]=v[i][j];
			}
		}
		sort(ans,ans+cnt);
		int i=0;
		for(;i<cnt-1;++i)
			if(ans[i]==ans[i+1])
				break;
		cnt=unique(ans,ans+cnt)-ans;
		printf("Case #%d: ",cas++);
		if(cnt==7)
			printf("%d\n",ans[i]);
		else if(cnt==8)
			printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
}