#include<bits/stdc++.h>

using namespace std;
int arr[2501];
int main(){
	int t,i,j,k,l,c,n;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d",&n);
		for(j=1;j<=2500;j++){
			arr[j]=0;
		}
		for(j=0;j<2*n-1;j++){
			for(k=0;k<n;k++){
				scanf("%d",&l);
				arr[l]++;
			}
		}
		printf("Case #%d: ",i);
		for(j=1;j<=2500;j++){
			if(arr[j]%2){
				printf("%d ",j);
			}
		}
		printf("\n");
	}
	
	return 0;
	
}
