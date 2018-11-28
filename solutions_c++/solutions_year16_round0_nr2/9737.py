#include<stdio.h>
#include<string.h>

void reverse(int a[],int n,int i){
	int j;
	for(j=i;j<n;j++){
		if(a[j]==1){
			a[j]=0;
		}
		else{
			a[j]=1;
		}
	}
}



int main(){

	int t;
	
	scanf("%d",&t);
	int n=t;
	while(t--){
	printf("Case #%d: ",n-t);
	char s[100];
	int i,a[100];
	scanf("%s",s);
	int n=strlen(s);
	if(n==1){
		if(s[0]=='+'){
			printf("0\n");
		}
		else{
			printf("1\n");
		}
		continue;
	}
	
	for(i=0;i<n;i++){
		if(s[n-1-i]=='+'){
			a[i]=1;
		}
		else{
			a[i]=0;
		}
	}
	int count=0;
	int k=0;
	while(k<(n-1)){
		if(a[k]==0){
			reverse(a,n,k);
			count++;
		}
		else{
			int r=0;
			while(a[k+r]==1 && k+r<n){
				r++;
			}
			if(k+r==(n)){
				break;
				
			}
			reverse(a,n,k+r);
			k=k+r;
			count++;
		}
	}
	printf("%d\n",count);
}
}
