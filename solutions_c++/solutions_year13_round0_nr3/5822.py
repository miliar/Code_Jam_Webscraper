#include<stdio.h>
#include <cmath>


int PerfectSquare(unsigned long long n)
{
    unsigned long long h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        unsigned long long t = (unsigned long long) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}

int check_for_pallindrome(unsigned long long n){
	unsigned long long num, rev;
	rev = 0;
	num = n;
	while (num != 0)
    {
         /*digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;*/
         rev = rev * 10;
         rev = rev + num%10;
         num = num/10;
    }
     if(n == rev)
     	return 1;
     else
     	return 0;
}

int main(){
	unsigned long long A, B, j, count;
	long long n, i;
	int pal, sq_pal;
	scanf("%lld", &n);
	for(i=1; i<=n ; i++){
		scanf("%llu %llu", &A, &B);
		count=0;
		for(j=A; j<=B; j++){
			pal = check_for_pallindrome(j);
			if(PerfectSquare(j))
				sq_pal = check_for_pallindrome(sqrt(j));
			else
				sq_pal = 0;
			if((pal==1) && (sq_pal==1))
				count++;
		}
		printf("Case #%lld: %llu\n", i, count);
	}
	return 0;
}
