#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int N=6;
int map1[N][N],map2[N][N];
bool hash[3*N];
int main(){
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int T,k=1;
	scanf("%d",&T);
	while(T--){
		memset(hash,0,sizeof(hash));
		int l,i,j;
		scanf("%d",&l);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&map1[i][j]);
				if(i==l) hash[map1[i][j]]=true;
			}
		}
		scanf("%d",&l);
		int ans=0,p;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&map2[i][j]);
				if(i==l) {
					if(hash[map2[i][j]])
					{ans++;p=map2[i][j];}
				}
			}
		}
		printf("Case #%d: ",k++);
		if(ans==0) printf("Volunteer cheated!\n");
		else if(ans==1) printf("%d\n",p);
		else printf("Bad magician!\n");
	}
	return 0;
}