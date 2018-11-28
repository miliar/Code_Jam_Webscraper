#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int f[1001][1001];
int a[1001],b[1001];
int bo[1001];

int abs(int x) { return x<0?-x:x;}

void swap(int &a,int &b){
	int t=a; a=b; b=t;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T=1,ca=0;
	scanf("%d",&T);
	while (T--){
		memset(f,63,sizeof(f));
		int n;
		scanf("%d",&n);
		for (int i=1; i<=n; ++i) scanf("%d",&a[i]);
		for (int i=1; i<=n; ++i) b[i]=a[i];
		sort(b+1,b+1+n);
		for (int i=1; i<=n; ++i)
			a[i]=lower_bound(b+1,b+1+n,a[i])-b;
		for (int i=1; i<=n; ++i)
			bo[a[i]]=i;
		f[0][0]=0;
		for (int i=0; i<n; ++i){
			for (int j=0; j<=i; ++j){
				f[i+1][j+1]=min(f[i+1][j+1],f[i][j]+abs(bo[i+1]-1));
				f[i+1][j]=min(f[i+1][j],f[i][j]+abs(bo[i+1]-(n-i)));
			}
			int k=0;
			for (int j=1; j<=n; ++j)
				if (a[j]==i+1) k=j;
			while (k<n){
				swap(a[k],a[k+1]);
				++k;
			}
			for (int j=1; j<=n; ++j) bo[a[j]]=j;
		}
		int ans=1000000000;
		for (int i=0; i<=n; ++i) ans=min(ans,f[n][i]);
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}
