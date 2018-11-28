#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

int arr1[5][5],arr2[5][5];

int main(){
	int t,l=0;
	scanf("%d",&t);
	while(l++<t){
		int ans1,ans2,n,i,j,cnt=0;
		scanf("%d",&ans1);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&arr1[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&arr2[i][j]);
			}
		}
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(arr1[ans1][i]==arr2[ans2][j]){
					cnt++;
					n=arr1[ans1][i];
				}
			}
		}
		printf("Case #%d: ",l);
		if(!cnt)
			printf("Volunteer cheated!\n");
		else if(cnt==1)
			printf("%d\n",n);
		else
			printf("Bad magician!\n");
	}
	return 0;
}