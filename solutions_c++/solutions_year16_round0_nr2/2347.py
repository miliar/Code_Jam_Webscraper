#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<cstdlib>
#include<algorithm>
using namespace std;

#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

#define maxn 110

char a[maxn];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	FOR(Tcase,1,T)
	{
		printf("Case #%d: ",Tcase);
		scanf("%s",a);
		int n=strlen(a);
		int ans=0;
		bool flag=false;
		FORD(i,n-1,0)
		{
			if (a[i]=='-') flag=true;
			if (flag && (i==n-1 || a[i]!=a[i+1])) ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}

