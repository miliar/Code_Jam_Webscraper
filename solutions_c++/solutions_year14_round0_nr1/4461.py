#include <stdio.h>
#include <cmath>
#include <cstring>

using namespace std;

int main(){
	int t,z,a,ans,c;
	int count [17];
	scanf("%d",&t);
	for(int j=1;j<=t;j++){
		memset(count,0,sizeof(count));
		scanf("%d",&a);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&z);
				if(i==a-1){
					count[z]++;
				}
			}
		}
		scanf("%d",&a);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&z);
				if(i==a-1){
					count[z]++;
				}
			}
		}
		c = 0;
		for(int i=0;i<17;i++){
			if(count[i]==2){
				c++;
				ans = i;
			}
		}
		printf("Case #%d: ", j);
		if(c==0){
			printf("Volunteer cheated!\n");
		} else if (c>1){
			printf("Bad magician!\n");
		} else if (c==1){
			printf("%d\n",ans);
		}
	}
}