#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int arr1[5][5],arr2[5][5];
int temp1[5],temp2[5];
int main(){
	//freopen("A-small-attempt3.in","r",stdin);
	//freopen("A-small-attempt3.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		memset(arr1,0,sizeof(arr1));
		memset(arr2,0,sizeof(arr2));
		memset(temp1,0,sizeof(temp1));
		memset(temp2,0,sizeof(temp2));
		int a1,a2;
		scanf("%d",&a1);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&arr1[i][j]);
				if(a1==i){
					temp1[j]=arr1[i][j];
				}
			}
		}
		scanf("%d",&a2);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&arr2[i][j]);
				if(a2==i){
					temp2[j]=arr2[i][j];
				}
			}
		}
		int k=0;int ik;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(temp1[i]==temp2[j]){
					++k;ik=temp2[j];
				}
			}
		}
		if(k==1){
			if(t==T) printf("Case #%d: %d",t,ik);
			else printf("Case #%d: %d\n",t,ik);
		}
		if(k>1){
			if(t==T) printf("Case #%d: Bad magician!",t);
			else printf("Case #%d: Bad magician!\n",t);
		}
		if(k==0){
			if(t==T) printf("Case #%d: Volunteer cheated!",t);
			else printf("Case #%d: Volunteer cheated!\n",t);
		}
	}
	return 0;
}
