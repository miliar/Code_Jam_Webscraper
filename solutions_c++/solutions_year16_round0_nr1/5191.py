#include <bits/stdc++.h> 

using namespace std; 
bool compare(int a, int b){
	return b<a;
}
int a[1000],b[1000];
int main(){
	int t,i,j,n,m,k;
	scanf("%d",&t);
	char s[20];
	for(i=1;i<=t;i++){
		scanf("%d",&n);
		int arr[10]={0};
		for(j=1;j<=101;j++){
			m = j*n ;
			sprintf(s,"%d",m);
			for(k=0;s[k]!='\0';k++){
				arr[s[k]-'0']++;
			}
			for(k=0;k<10;k++){
				if(arr[k]==0)break;
			}
			if(k==10){
				printf("Case #%d: %d\n",i,m);
				break;
			}
		}
		if(j==102){
			printf("Case #%d: INSOMNIA\n",i);
		}
	}
	return 0;
}