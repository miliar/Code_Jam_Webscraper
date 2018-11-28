#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

int cartas[5][5];
int cartas2[5][5];

int main(){

	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);

	
	int t;
	
	scanf("%d",&t);
	
	
	for(int c=0;c<t;c++){
		int f1,f2;
		scanf("%d",&f1);
		f1--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&cartas[i][j]);
			}
		}
		
		scanf("%d",&f2);
		f2--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&cartas2[i][j]);
			}
		}
		
		int cont=0;
		int val;
		for(int i=0;i<4;i++){
			
			for(int j=0;j<4;j++){
				if(cartas2[f2][i]==cartas[f1][j]){
					cont++;
					val=cartas2[f2][i];
				}
			}
		}
		
		if(cont==0){
			printf("Case #%d: Volunteer cheated!\n",c+1);
		}else if(cont==1){
			printf("Case #%d: %d\n",c+1,val);
		}else{
			printf("Case #%d: Bad magician!\n",c+1);
		}
		
		
	}
	
	
}