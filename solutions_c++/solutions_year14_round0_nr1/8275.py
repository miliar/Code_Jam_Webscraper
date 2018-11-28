#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	int a1[5][5],a2[5][5];
	int ans1,ans2;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		scanf("%d",&ans1);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a1[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a2[i][j]);
			}
		}
		int count = 0;
		int val = -1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a1[ans1-1][i] == a2[ans2-1][j]){
					count++;
					val = a1[ans1-1][i];
				}
			}
		}
		if(count == 0){
			printf("Case #%d: Volunteer cheated!\n",k);
		} else if (count == 1){
			printf("Case #%d: %d\n",k,val);
		} else {
			printf("Case #%d: Bad magician!\n",k);
		}
	}
	return 0;
}