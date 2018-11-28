#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int x,n;
int s[10010];

int main()
{
	freopen("A-large.in","rb",stdin);
	freopen("test.out","wb",stdout);
	int T,cas=1;scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",cas++);
		scanf("%d%d",&n,&x);
		for(int i=0;i<n;++i) scanf("%d",&s[i]);
		sort(s,s+n);
		int l=0,r=n-1,ans=0;
		while(l<=r){
			if(l==r) ++ans,--r;
			else if(s[l]+s[r]<=x) ans++,++l,--r;
			else ans++,--r;
		}
		printf("%d\n",ans);
	}
	return 0;
}
