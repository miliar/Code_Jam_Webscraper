#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <memory.h>
#include <iostream>
#include<list>
using namespace std;

#define pb push_back
#define sz size()
#define mp make_pair
#define mset(ar,val) memset(ar,val,sizeof ar)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))


void scan(int* i) {int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}
void scan(long long int* i) {long long int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}

#define pi 3.14
int main() {
	int x,T,count;
	unsigned long long r,j,i,t,k;
	scan(&T);
	for(x=1;x<=T;++x){
		count=0;
		scanf("%lld",&r);
		scanf("%lld",&t);
		j=t;
		k=r;
		unsigned long long potential;
		while(1){
			potential=((pow(k+1,2)-pow(k,2)));
			if((int)potential <= j){
				++count;
				j-=potential;
				k+=2;
			}
			else break;
		}
		printf("Case #%d: %d\n",x,count);
	}
	return 0;
}

