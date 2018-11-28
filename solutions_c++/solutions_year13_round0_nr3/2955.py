#include <stdio.h>
#include <math.h>

bool isPalindrome(int num){
	int i, len;
	int digit[10];
	for(i=0;i<10 && num>0;i++, num/=10)
		digit[i] = num%10;

	len = i-1;
	for(i--; i>len/2; i--)
		if(digit[i]!=digit[len-i])
			return false;
	return true;
}

bool isFairAndSquare(int num){
	int root= (int) sqrt((double) num);
	if(root*root != num)
		return false;

	if(isPalindrome(num) && isPalindrome(root))
		return true;
	return false;
}

void solve(){
	int a, b, i;
	int count=0;

	scanf("%d %d", &a, &b);
	for(i=a;i<=b;i++)
		if(isFairAndSquare(i))
			count++;

	printf("%d", count);
}

int main(int argc, char *argv[]){
	int t, T;
	scanf("%d", &T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}
