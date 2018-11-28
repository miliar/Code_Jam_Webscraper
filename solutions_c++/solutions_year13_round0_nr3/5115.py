/*
 * =====================================================================================
 *
 *       Filename:  C.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 14:00:00
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Cong Zhao (), zhaocong89@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define FF(i,n) for(int(i)=0;(i)<(n);(i)++)
#define FOR(i,l,h) for(int(i)=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define CC(n,what) memset(n,what,sizeof(n))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int isPalindrome(long long num){
	char ss[20];
	int pos = 0;
	memset(ss, 0, sizeof(ss));
	while(num){
		ss[pos++] = num%10 + '0';
		num/=10;		
	}
	int result = 1;
	int len = strlen(ss);
	for(int i = 0; i < len / 2; i++){
		if(ss[i] != ss[len - i - 1]){
			result = 0;
			break;
		}
	}
	return result;
}

long long isPal[45];
long long square[45];

int main(){
	int ncase = 0;
	int tmptotal = 0;
	scanf("%d", &ncase);
	memset(isPal, 0 ,sizeof(isPal));
	for(long long tmp = 1; tmp <= 10000000; tmp++){
		if(isPalindrome(tmp) && isPalindrome(tmp * tmp)){
			isPal[tmptotal++] = tmp;
		}	
	}

	for(int i = 0; i < tmptotal; i++){
		square[i] = isPal[i] * isPal[i];
	}
		
	for(int nn = 1; nn <= ncase; nn++){
		long long a,b;
		long long total = 0;
		scanf("%lld%lld", &a, &b);
		for(int i = 0; i < tmptotal; i++){
			if(square[i] >= a && square[i] <= b){
				total++;
			}
		}
		printf("Case #%d: %lld\n", nn, total);
	}
}
