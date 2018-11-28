#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int a[10][10];
bool f[20];
int main(){
	int cases,n,m;
	freopen("A-small-attempt4.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d",&n);
		memset(f,false,sizeof(f));
		for (int i=1;i<=4;i++){
			for (int j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
				if (n==i) f[a[i][j]]=true;
			}
		}
		scanf("%d",&m);
		int ans=0;int k;
		for (int i=1;i<=4;i++){
			for (int j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
				if (m==i&&f[a[i][j]]) {
					ans++;
					k=a[i][j];
				}
			}
		}
		if (ans==1) printf("Case #%d: %d\n",cas,k);
		else if (ans==0) printf("Case #%d: Volunteer cheated!\n",cas);
		else printf("Case #%d: Bad magician!\n",cas);
	}
	return 0;
}
