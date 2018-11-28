#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,m1,m2,count,c;
	int a[4][4];
	int b[4][4];
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&m1);
	//	cout<<m1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&a[j][k]);
			}
		}
		scanf("%d",&m2);
	//	cout<<m2;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&b[j][k]);
			}
		}
		count=0;
	//	for(int j=0;j<4;j++) cout<<a[m1-1][j]<<" ";
	//	for(int j=0;j<4;j++) cout<<a[m1-1][j]<<" ";
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(a[m1-1][j]==b[m2-1][k]){
					c=a[m1-1][j];
					count++;
				}
			}
		}
		if(count==0)
			printf("Case #%d: Volunterr Cheated!\n",i);
		else if(count==1)
			printf("Case #%d: %d\n",i,c);
		if(count>1)
			printf("Case #%d: Bad Magician!\n",i);

	}
}