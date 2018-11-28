#include <stdio.h>
#include <stdlib.h>
#include <math.h>

bool isPalindrome(unsigned long long int num){
	int i =0,j=0;
	char* buff = NULL;
	unsigned long long temp = num;
	int numDigits = 0;
	bool res;
	
	while(temp != 0){
		temp = temp/10;
		numDigits++;
	}
	buff = (char*)malloc(sizeof(char)*numDigits);
	i = 0;
	temp = num;
	while(temp != 0){
		buff[i] = temp%10;
		temp = temp/10;
		i++;
	}
	i =0;
	j = numDigits-1;
	res = true;
	while(i<=j){
		if(buff[i] != buff[j]) res = false;
		i++;
		j--;
	}
	return res;
	
}

int main(void){
	FILE* inp = fopen("inp.txt","r");
	FILE* out = fopen("out.txt","w");
	unsigned long long int a =0;
	unsigned long long int b =0;
	int t =0;
	int numCase = 1;
	int low,high;
	long double intpart,fractpart;
	int i =0;
	int ans;
	/*
	while(true){
		printf("enter :");
		scanf("%llu",&n);
		if(isPalindrome(n)) printf("palindrome\n");
		else printf("not palindrome\n");
	}
	*/
	fscanf(inp,"%d",&t);
	for(numCase = 1;numCase<=t;numCase++){
		fscanf(inp,"%llu",&a);
		fscanf(inp,"%llu",&b);
		fractpart = modf (sqrt((long double)a) , &intpart);
		if(fractpart == 0.0) low = (int )intpart;
		else low = (int )intpart +1;
		
		fractpart = modf (sqrt((long double)b) , &intpart);
		high = (int)intpart;
		ans = 0;
		for(i=low;i<=high;i++){
			if(isPalindrome(i) && isPalindrome((unsigned long long int)i*i)) {
				ans++;
			}
		}
		fprintf(out,"Case #%d: %d\n",numCase,ans);

	}
}
