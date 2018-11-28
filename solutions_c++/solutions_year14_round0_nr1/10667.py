#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){

	int cases;
	int arr1[16];
	int arr2[16];
	int aux1[4];
	int aux2[4];
	int same[4];
	
	int ans1;
	int ans2;
	
	int cont;
	int num = 1;
	int contsame=0;
	
	int in1;
	int in2;
	
	//1* 0-3 
	//2* 4-7
	//3* 8-11
	//4* 12-15
	
	scanf("%d",&cases);
	
	while(cases>0){
	
		cont = 0;
		contsame = 0;
		in1=0;
		in2=0;
		
		scanf("%d",&ans1); //first ans
		
		for(int i = 0; i<16;i++){ //first arrangement
			scanf("%d",&arr1[i]);
		}
			
		switch(ans1){
			case 1: 
				for(int i = 0; i<=3;i++){
					aux1[i]=arr1[i];
				}
			break;
			case 2:
				for(int i = 4;i<=7;i++){
					aux1[in1]=arr1[i];
					in1++;
				}
			break;
			case 3:
				for(int i = 8; i <=11; i++){
					aux1[in1]=arr1[i];
					in1++;
				}
			break;
			case 4:
				for(int i = 12; i<=15; i++){
					aux1[in1]=arr1[i];
					in1++;
				}
			break;
		}
		
		scanf("%d",&ans2); //second ans
		
		for(int i = 0; i<16; i++){ //second arrangement
			scanf("%d",&arr2[i]);
		}
			
		switch(ans2){
			case 1: 
				for(int i = 0; i<=3;i++){
					aux2[i]=arr2[i];
				}
			break;
			case 2:
				for(int i = 4;i<=7;i++){
					aux2[in2]=arr2[i];
					in2++;
				}
			break;
			case 3:
				for(int i = 8; i <=11; i++){
					aux2[in2]=arr2[i];
					in2++;
				}
			break;
			case 4:
				for(int i = 12; i<=15; i++){
					aux2[in2]=arr2[i];
					in2++;
				}
			break;
		}
			
		for(int i = 0; i<4; i++){
			for(int j = 0; j<4; j++){
				if(aux1[i]==aux2[j]){
					cont++;
					same[0]=aux2[j];
					break;
					
				}
			}
		}
		
		switch(cont){
			case 0:
				printf("Case #%d: Volunteer cheated!\n",num);
			break;
			case 1:
				printf("Case #%d: %d\n",num,same[0]);
			break;
			default:
				printf("Case #%d: Bad magician!\n",num);
			break;
		}
		
		
		cases--;
		num++;
	}
	

}