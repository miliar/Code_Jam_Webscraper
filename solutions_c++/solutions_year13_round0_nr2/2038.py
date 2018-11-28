#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	int C;
	scanf("%d",&C);
	for(int Case=1;Case<=C;Case++){
		int n,m,a[101][101]={};
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++){
				a[i][0]=max(a[i][0],a[i][j]);
				a[0][j]=max(a[0][j],a[i][j]);
			}			
		bool ok=true;
		for(int i=1;i<=n && ok;i++)
			for(int j=1;j<=m && ok;j++)
				if(min(a[i][0],a[0][j])>a[i][j])
					ok=false;
		printf("Case #%d: %s\n",Case,ok?"YES":"NO");
	}
}
