#include <cstdio>
#include <set>
using namespace std;
set<int> bee;
int t[20][20];
int june,a,r;
int res=0;
int poi=1;
int i,j;
int a1,a2,a3,a4,a5,a6,a7,a8,a9,a10;
void go(){
	scanf("%d",&r);
	while(r--){
		bee.clear();
		scanf("%d",&a);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&t[i][j]);
				if(i==a) bee.insert(t[i][j]);
			}
		}
		june=0;
		res=0;
		scanf("%d",&a);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&t[i][j]);
				if(i==a){
					if(bee.find(t[i][j])!=bee.end()){
						june++;
						res=t[i][j];
					}
				}
			}
		}
		printf("Case #%d: ",poi++);
		if(june==0) printf("Volunteer cheated!\n");
		else if(june==1) printf("%d\n",res);
		else printf("Bad magician!\n");
	}
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	go();
	return 0;
}