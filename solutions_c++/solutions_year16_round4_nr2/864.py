#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

double f[18][18],p[210],ans;
int T,t,n,m,k,i,j,d,e,b[1<<18],a[18];

int main() {
	b[0]=0;
	for (i=1;i<(1<<16);i++)
	b[i]=b[i/2]+i%2;
	cin>>T;
	for (t=1;t<=T;t++) {
		cin>>n>>m;
		for (i=0;i<n;i++)
		cin>>p[i];
		ans=0;
		for (d=0;d<(1<<n);d++)
		if (b[d]==m) {
			e=0;
			for (i=0;i<n;i++)
			if ((d&(1<<i))==(1<<i))
			a[++e]=i;
			memset(f,0,sizeof(f));
			f[0][0]=1;
			for (i=1;i<=m;i++) {
				f[i][0]=f[i-1][0]*(1-p[a[i]]);
				for (j=1;j<=m/2;j++) {
					f[i][j]=f[i-1][j]*(1-p[a[i]])+f[i-1][j-1]*p[a[i]];
				}
			}
			ans=max(ans,f[m][m/2]);
		}
		printf("Case #%d: %.8f\n",t,ans);
	}
    return 0;
}
