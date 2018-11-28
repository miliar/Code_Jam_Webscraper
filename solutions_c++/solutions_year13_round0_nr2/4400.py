#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
int i,T,j,a[120][120],flag,k,tim,n,m;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	for(scanf("%d",&T),tim=1;tim<=T;++tim){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;++i)
			for(j=1;j<=m;++j)scanf("%d",&a[i][j]);
		printf("Case #%d: ",tim);
		for(i=1;i<=n;++i){
			for(j=1;j<=m;++j){
				flag=0;
				for(k=1;k<=m;++k)if(a[i][k]>a[i][j])flag|=1;
				for(k=1;k<=n;++k)if(a[k][j]>a[i][j])flag|=2;
				if(flag==3){
					printf("NO\n");
					goto aaa;
				}
			}
		}
		printf("YES\n");
		aaa:;
	}
}
