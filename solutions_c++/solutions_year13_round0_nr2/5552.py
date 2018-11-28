#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int a[200][200];

int main(){
	int T,n,m;
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		bool can=true;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				bool f1=true,f2=true;
				for (int k=0;k<n;k++)
					if (a[k][j]>a[i][j]) f1=false;
				for (int k=0;k<m;k++)
					if (a[i][k]>a[i][j]) f2=false;
				if (!f1&&!f2){
					can=false; break;
				}
			}
		if (can) printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}
