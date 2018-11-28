#include <iostream>
#include <string.h>
using namespace std;

int v[20];
int t,ans1,tmp;

int main(){
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&t);
	for ( int i = 1; i <= t; ++ i){
		printf("Case #%d: ",i);
		memset(v,0,sizeof(v));
		scanf("%d",&ans1);
		for ( int j = 1; j <= 4; ++ j){
			for ( int k = 1; k <= 4; ++ k){
				scanf("%d",&tmp);
				if (j == ans1) ++ v[tmp];
			}
		}
		scanf("%d",&ans1);
		for ( int j = 1; j <= 4; ++ j){
			for ( int k = 1; k <= 4; ++ k){
				scanf("%d",&tmp);
				if (j == ans1) ++ v[tmp];
			}
		}
		tmp = 0;
		for ( int j = 1; j <= 16; ++ j){
			if (v[j] == 2){
				if (tmp){
					printf("Bad magician!\n");
					tmp = 20;
					break;
				}
				else
					tmp = j;
			}
		}
		if (!tmp){
			printf("Volunteer cheated!\n");
		}
		else
		if (tmp < 20) printf("%d\n",tmp);
	}
}
