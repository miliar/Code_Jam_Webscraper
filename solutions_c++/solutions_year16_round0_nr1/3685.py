/*
 * cjam.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: rss
 */
#define gc() (*_pinp?*_pinp++:(_inp[fread(_pinp=_inp, 1, 4096, stdin)]='\0', *_pinp++))
char _inp[4097], *_pinp=_inp, _; bool _ssign;
#define nextInt(x) do{while((x=gc())<'-'); _ssign=x=='-'; if(_ssign) while((x=gc())<'0'); for(x-='0'; '0'<=(_=gc()); x=(x<<3)+(x<<1)+_-'0'); x=_ssign?-x:x;}while(0)
#include <cstdio>
#include <bitset>
#include <iostream>
using namespace std;
int T, N, K, D; bitset<10> bset; bool k;
int main() {
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		scanf("%d", &N);
		bset.set();
		for (int i=1; i<3000; i++) {
			K=i*N;
			while (K>0) {
				D=K%10;
				bset[D]=0;
				K=K/10;
			}
			if (bset.none()) {
				printf("Case #%d: %d\n", t, i*N);
				k=1;
				break;
			}
		}
		if (!k) printf("Case #%d: INSOMNIA\n", t);
	}

	return 0;
}
