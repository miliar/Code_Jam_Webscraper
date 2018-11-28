/*
 * =====================================================================================
 *
 *       Filename:  palin.cc
 *
 *    Description:  Palindrome
 *
 *        Version:  1.0
 *        Created:  04/13/2013 07:09:43 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jan Sebechlebsky (js), sebecjan@fit.cvut.cz
 *        Company:  Faculty of Information Technology, CTU Prague
 *
 * =====================================================================================
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

bool isPalindrome(long num) {
	char cislo[32];
	//ltoa( num, cislo, 10 );
	sprintf( cislo, "%ld",num);
	int len = strlen(cislo);
	if( len == 1 ) return true;
	int len2 = len >> 1;
	for( int i = 0; i < len2; i++ ) {
		//printf( "%c %c\n", cislo[i],cislo[i])
		if( cislo[i] != cislo[len - i - 1] )return false;
	}
	return true;
}

vector<long> nums;

void precalc() {
	for( long i = 1; i < 10000000; i++ ) {
		long p = i*i;
		if( isPalindrome(i) && isPalindrome(p) )
			nums.push_back(p); 
	}
}

int main() {
	precalc();
	//printf("%d",nums.size());
	int t = 0;
	scanf("%d",&t);
	for( int c = 1; c <= t; c++ ) {
		long a,b,res = 0;
		scanf("%ld%ld",&a,&b);
		for( vector<long>::iterator it = nums.begin(); it!=nums.end(); it++ ) {
			if( *it > b )break;
			if( *it >= a ){
	//			printf("%ld\n",*it);
			res++;}
		}
		printf("Case #%d: %ld\n",c,res);
	}
	return 0;
}
