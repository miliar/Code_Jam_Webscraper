#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
int arr1[4][4];
int arr[16]={0};
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc,x;
	scanf("%d",&tc);
	for(int k=1;k<=tc;k++){
		for(int i=0;i<16;i++){
			arr[i] = 0;
		}
		scanf("%d",&x);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&arr1[i][j]);
				arr1[i][j]--;
			}
		}
		x--;
		for(int i=0;i<4;i++){
			arr[arr1[x][i]]++;
		}
		scanf("%d",&x);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&arr1[i][j]);
				arr1[i][j]--;
			}
		}
		x--;
		for(int i=0;i<4;i++){
			arr[arr1[x][i]]++;
		}
		int cnt = 0,num;
		for(int i=0;i<16;i++){
			if(arr[i]>1){
				num = i+1;
				cnt++;
			}
		}
		if(cnt == 1){
			printf("Case #%d: %d",k,num);
		}
		else if(cnt == 0){
			printf("Case #%d: Volunteer cheated!",k);
		}
		else{
			printf("Case #%d: Bad magician!",k);
		}
		printf("\n");	
	}
	return 0;
}
