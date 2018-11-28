#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int a[5][5],b[5][5];
int main(){
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		int ans1,ans2,x,i,j;
		scanf("%d",&ans1);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&b[i][j]);
			}
		}
		int c=0,ans;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(a[ans1][i]==b[ans2][j]){
					ans=a[ans1][i];
					++c;
					break;
				}
			}
		}
		if(c==1)
			printf("Case #%d: %d\n",k,ans);
		else if(!c)
			printf("Case #%d: Volunteer cheated!\n",k);
		else
			printf("Case #%d: Bad magician!\n",k);
	}
	return 0;
}
