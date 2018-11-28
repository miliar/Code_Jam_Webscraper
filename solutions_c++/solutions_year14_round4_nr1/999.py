#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#define X first
#define Y second
#define fo(i,n) for(int i=0;i<n;i++)
#define fr(i,n) for(int i=1;i<=n;i++)
#define pb push_back

using namespace std;

typedef long long ll;

const int mod=(int)1e9+7;

int T,n,m,v[10010],a[10010],cas;

int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		fr(i,n)
			scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		memset(v,0,sizeof v);
		int ans=n,j=n;
		for(int i=1;i<=n;i++){
			while(i<j&&a[i]+a[j]>m) j--;
			if(i<j) j--,ans--;
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}

