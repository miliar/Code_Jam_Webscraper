#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string>

using namespace std;

int isPalindrome(long long n){
	char arr[200];
	sprintf(arr,"%lld",n);
	string s(arr);
	for(string::iterator left=s.begin(),right=s.end()-1;left<right;left++,right--)
		if(*left!=*right)
			return 0;
	return 1;
}

int main(){
	int T,i;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		long long A,B,x;
		scanf("%lld %lld",&A,&B);
		x=(long long)sqrt(A);
		while(x*x<A)
			x++;
		long long count=0;
		for(;x*x<=B;x++){
			if(isPalindrome(x)&&isPalindrome(x*x)){
				count++;
			}
		}
		printf("%lld\n",count);
	}
}
