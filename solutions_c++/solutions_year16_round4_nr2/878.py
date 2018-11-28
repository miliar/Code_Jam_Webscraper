#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <set>
#include <limits>
#include <bitset>
using namespace std;

#define FOR(i,f,t) for(int i=f; i<t; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define pb push_back
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d %d", &x, &y)
#define SYNC ios_base::sync_with_stdio(false)

typedef long long ll;

int const MAXN = 202;

double p[MAXN];
int N, K;


uint next_mask(uint mask){
	uint t = mask | (mask - 1);
	return  (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(mask) + 1));
}



int main(){
	int TC; ri(TC);
	FOR(tc,1,TC+1){
		rii(N, K);
		FOR(i,0,N) scanf("%lf",&p[i]);
		int n=N, m=K;
		int mask=(1<<m)-1; // mask es el comite de K personas
		double ans = 0;
		for(int mask=(1<<m)-1; !(mask & (1<<n)); mask=next_mask(mask)){
			double nans = 0;
			for(int sub = (mask-1) & mask ; sub; sub = (sub-1) & mask ){ // sub son los que dicen que si
				if(__builtin_popcount(sub) == K/2){
					double P = 1;
					FOR(i,0,N) if(mask & (1<<i)){
						if(sub & (1<<i)){
							P*=p[i];
						}else{
							P*=(1-p[i]);
						}
					}
					nans += P;
				}
			}
			ans = max(ans, nans);
		}			
		printf("Case #%d: %.8lf\n",tc,ans);
	}
	
}

