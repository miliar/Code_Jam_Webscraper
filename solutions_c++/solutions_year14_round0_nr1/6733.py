#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);
	int arr1[4][4],arr2[4][4];
	int ans1,ans2;
	int num,count;
	int temp;
	for(int i=1;i<=T;i++){
		scanf("%d",&ans1);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&arr1[j][k]);
			}
		}
		scanf("%d",&ans2);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&arr2[j][k]);
			}
		}
		num=0;
		count=0;
		for(int j=0;j<4;j++){
			temp=arr1[ans1-1][j];
			for(int k=0;k<4;k++){
				if(arr2[ans2-1][k]==temp){
					count++;
					num=temp;
					break;
				}
			}
		}
		if(count==0){
			printf("Case #%d: Volunteer cheated!\n",i);
		}
		else if(count==1){
			printf("Case #%d: %d\n",i,num);
		}
		else{
			printf("Case #%d: Bad magician!\n",i);
		}
	}
	return 0;
}
