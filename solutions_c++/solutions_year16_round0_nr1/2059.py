#include<bits/stdc++.h>
using namespace std;

void markDigit(int n, int digit[10]){
	while(n){
		digit[n%10]=1;
		n=n/10;
	}
}

int checkAllMarked(int digit[10]){
	for(int i=0;i<10;i++){
		if(digit[i]==0)
			return 0;
	}
	return 1;
}

int main(){
	int t,n,cas,digit[10],i;
	scanf("%d",&t);

	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",cas);
			continue;
		}

		// initialise digit
		for(i=0;i<10;i++)
			digit[i]=0;
		
		// get the digits
		for(i=1;;i++){
			markDigit(n*i, digit);
			if(checkAllMarked(digit))
				break;
		}
		printf("Case #%d: %d\n",cas,n*i);
	}
	return 0;
}