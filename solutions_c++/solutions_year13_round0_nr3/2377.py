#include <cstdio>
#include <cmath>

#define MAXN 10000005
using namespace std;
typedef unsigned long long uLong;

bool isPalindrome(uLong num){
	uLong rev = 0, mn=num;
	while( num>0 ){
		rev = 10*rev + (num%10);
		num /= 10;
	}
	return mn==rev;
}

int countFairSqPal[MAXN];

int main(){
	freopen("C:\\googlecj\\C-large-1.in", "r", stdin);
	freopen("C:\\googlecj\\C-large-1.out", "w", stdout);
	uLong a, b, i, sq, fsqCount;
	int tc, caseNum=1;
	for(uLong i=1; i<MAXN; i++){
		countFairSqPal[i] = countFairSqPal[i-1];
		if(isPalindrome(i)){
			a = i*i;
			if(isPalindrome(a))
				countFairSqPal[i] ++;
		}
	}

	scanf("%d", &tc);
	while( tc-- ){
		scanf("%llu %llu", &a, &b);
		sq = sqrt(a);
		if( (sq*sq)==a)
			a = sq-1;
		else
			a = sq;
		b = sqrt(b);

		printf("Case #%d: %d\n", caseNum++, countFairSqPal[b]-countFairSqPal[a]);
	}

	return 0;
}

