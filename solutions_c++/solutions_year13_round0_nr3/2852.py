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

int isPalindrome(int num){
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

int main(){
	int ncase = 0;
	scanf("%d", &ncase);
	for(int nn = 1; nn <= ncase; nn++){
		int a,b,c;
		int total = 0;
		scanf("%d%d", &a, &b);
		c = (int)sqrt(b);
		for(int num = ceil(sqrt(a)); num <= c; num++){
			if(isPalindrome(num) && isPalindrome(num * num)){
				total++;	
			}	
		}
		printf("Case #%d: %d\n", nn, total);
	}
}
