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

int T,n,a[1010],b[1010],c[1010],d[1010],f[1010][1010],cas;

int F(int l,int r){
	if(l>r) return 0;
	if(f[l][r]!=-1) return f[l][r];
	f[l][r]=min(F(l+1,r)+d[n-r+l],F(l,r-1)+r-l-d[n-r+l]);
	return f[l][r];
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]),b[i]=a[i];
		sort(b+1,b+n+1);
		memset(f,-1,sizeof f);
		memset(d,0,sizeof d);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				if(a[i]==b[j])
					c[i]=j;
		for(int i=1;i<=n;i++)
			for(int j=1;j<i;j++)
				if(a[j]>a[i])
					d[c[i]]++;
		printf("Case #%d: %d\n",++cas,F(1,n));
	}
	return 0;
}

