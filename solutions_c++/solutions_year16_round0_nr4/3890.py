#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 50500

#define count blergh

typedef long long ll;
using namespace std;

main(){

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ",t);
		if(s < k){
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(k == 1){
			printf("1\n");
			continue;
		}
		ll a = 1;
		for(int i=0;i<c;i++)
			a *= k;
		for(ll i = 1;i <= a; i += (a-1)/(k-1))
			printf("%lld ",i);
		printf("\n");
	}

}
