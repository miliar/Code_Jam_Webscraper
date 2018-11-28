#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t,c,x,y,num;
	scanf("%d",&t);
	int a[4][4];
	int b[4][4];
	for(int i = 0; i  < t; i++){
		c = 0;
		scanf("%d",&x);
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				scanf("%d",&a[j][k]);		
			}	
		}
		scanf("%d",&y);	
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				scanf("%d",&b[j][k]);		
			}	
		}	
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				if(a[x-1][j] == b[y-1][k]){
					c++;
					num = a[x-1][j];	
				}	
			}	
		}
		if(c == 1){
			printf("Case #%d: %d\n",i+1,num);	
		}else if(c == 0){
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}else{
			printf("Case #%d: Bad magician!\n",i+1);
		}
	}	
	return 0;
}
