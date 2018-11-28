#include <cstdio>
#include <cstring>
using namespace std;
int a[101][101],n,m,t;
bool chk;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i = 0; i < t; ++i){
		memset(a,0,sizeof a);
		scanf("%d%d",&n,&m);
		for (int j=0; j<n; j++){
			for (int k=0; k<m; k++){
				scanf("%d",&a[j][k]);
			}
		}
		chk=false;
		for (int j=0; j<n; j++){
			for (int k=0; k<m; k++){
				bool chk1=false,chk2=false;
				for (int l=0; l<m; l++){
					if (a[j][l]>a[j][k]) chk1=true;
				}
				for (int l=0; l<n; l++){
					if (a[l][k]>a[j][k]) chk2=true;
				}
				if (chk1&&chk2) chk=true;
			}
		}
		printf("Case #%d: ",i+1);
		if (chk) printf("NO\n");
		else printf("YES\n");
	}
}