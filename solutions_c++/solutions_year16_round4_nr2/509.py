#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

double f[250][450];
double a[250];
double b[250];
int n,k;

int main(){
	int T=0;
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d%d", &n,&k);
		for (int i=0; i<n; ++i)
			scanf("%lf", a+i);
		sort(a,a+n);
		double ans=0;
		for (int i=0; i<=k; ++i){
			for (int j=0; j<i; ++j) b[j]=a[j];
			for (int j=i; j<k; ++j) b[j]=a[n-1-j+i];
			memset(f,0,sizeof(f));
			f[0][k]=1;
			for (int i=0; i<k; ++i)
				for (int j=k-i; j<=k+i; ++j)
					if (f[i][j]>0){
						f[i+1][j+1]+=f[i][j]*b[i];
						f[i+1][j-1]+=f[i][j]*(1-b[i]);
					}
			if (f[k][k]>ans) ans=f[k][k];
		}
		printf("Case #%d: %.6f\n", t, ans);
	}
}

