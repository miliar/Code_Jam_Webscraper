#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int n;
typedef long long ll;
typedef __int128 int128;

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int t;
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		printf("Case #%d: ", _);
		ll p;
		scanf("%d %lld", &n, &p);
		ll resp = 1;
		resp <<= n;
		if(p >= resp-1){
			printf("%lld %lld\n", p-1, p-1);
			continue;
		}
		if(p == 1){
			printf("0 0\n");
			continue;
		}
		resp = 0;
		ll pot = 2;
		p--;
		for(int i = n-1; i >= 0; --i){
			if((p>>i)&1){
				resp += pot;
				pot <<= 1;
			}
			else break;
		}
		if(resp == 1) resp = 0;
		printf("%lld ", resp);
		////////////////
		p++;
		pot = 1;
		pot <<= n;
		p /= 2;
		resp = 0;
		while(p){
			p /= 2;
			pot /= 2;
			resp += pot;
		}
		printf("%lld\n", resp);
	}
	return 0;
}
