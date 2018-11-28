#include <cstdio>
#include <vector>
#include <string.h>
#include <cmath>

#define FOR(a,b) for(long long int a=0; a<b; a++)
#define MAX(a,b) ((a) < (b) ? (b) : (a))

using namespace std;

int T;

long long int A, B;

int isPalindrome(long long int a){
	char s[100];
	sprintf(s, "%lld", a);
	int l = strlen(s);
	FOR(i, l)
		if(s[i]!=s[l-i-1])
			return 0;
	return 1;
}

vector < long long int > them;

int main (){

	FOR(i, (long long int)1000*1000*100){
		if(isPalindrome(i) && isPalindrome(i*i))
			them.push_back(i*i);
//			printf("%lld %lld %f\n", i, i*i, 2*log(i)/log(10));
	}

	scanf("%d", &T);
	
	FOR(cas, T){
		scanf("%lld", &A);
		scanf("%lld", &B);
		
		int num=0;
		FOR(i, them.size())
			if(them[i]>=A && them[i]<=B)
				num++;
		
		printf("Case #%lld: %d\n", cas+1, num);	
	}
	return 0;
}
