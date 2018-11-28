#include <bits/stdc++.h>
using namespace std;
#define eprintf(...) fprintf(stderr,__VA_ARGS__)

const int N=205;

int n,k;

double p[N],q[N],f[N][N];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T; scanf("%d",&T);
	for(int Case=1;Case<=T;Case++){
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++) scanf("%lf",&p[i]);
		sort(p+1,p+n+1);
		double ans=0;
		for(int k=0;k<=::k;k++){
			for(int i=1;i<=k;i++) q[i]=p[i];
			for(int i=k+1;i<=::k;i++) q[i]=p[n-::k+i];
			f[0][0]=1;
			for(int i=1;i<=::k;i++)
				for(int j=0;j<=i;j++){
					f[i][j]=(f[i-1][j]*(1-q[i])+(j?f[i-1][j-1]:0)*q[i]);
				}
			ans=max(ans,f[::k][::k/2]);
		}
		printf("Case #%d: %.12lf\n",Case,ans);
	}
}