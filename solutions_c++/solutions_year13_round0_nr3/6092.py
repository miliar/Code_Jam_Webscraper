#include <cstdio>
#include <cmath>

bool isPalindrome(int target) {

	char chTar[10];
	int cn;

	for(cn=0; target!=0; ++cn, target/=10) chTar[cn]=target%10;

	for(int i=0; i<cn/2; ++i)
		if(chTar[i]!=chTar[cn-i-1]) return false;
	return true;

}

bool isSquare(int target) {

	int sqrtRes=sqrt((double)target);
	if(sqrtRes*sqrtRes!=target) return false;

	if(isPalindrome(sqrtRes)) return true;
	return false;

}

int main() {

	int T;
	int a, b;

	scanf("%d", &T);
	for(int i=1; i<=T; ++i) {

		scanf("%d %d", &a, &b);

		int res=0;
		for(int j=a; j<=b; ++j)
			if(isPalindrome(j) && isSquare(j)) ++res;

		printf("Case #%d: %d\n", i, res);

	}

	return 0;

}