#include<stdio.h>
#include<math.h>

int isPalindrome(int);

int main(){
	int T, teste=1;
	int A, B;
	char c;
	int i,j;
	int sq;
	int count;

	scanf("%d",&T);

	while(T--){
		scanf("%d %d",&A, &B);

		count = 0;

		sq = (int)sqrt(A);
		if(sq*sq < A) sq++;

		for(; sq<=sqrt(B); sq++){
			if(isPalindrome(sq) && isPalindrome(sq*sq)) count++;
		}

		printf("Case #%d: %d\n", teste++, count++);
	}

	return 0;
}

/* 
Checks for palindrome.
@params 1 <= X <=1000
Returns
1: yes
0: no
*/
int isPalindrome(int x){
	if(x<10) return 1;
	else if(x>=10 && x<100) return (int)(x/10) == x%10;
	else if(x>=100 && x<1000) return (int)(x/100) == x%10;
	return 0;
}

