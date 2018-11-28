// Omair Ali
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

#define SCS(s) assert(scanf("%s", s));
#define SCI(i) assert(scanf("%d", &i));
#define PRI(i) printf("%d\n", i);
#define PRM(s) printf("%s\n", s);
#define PRN printf("\n");
#define PRIM(s,i) printf("%s%d\n", s, i);
#define FOR(a,b) for(int a = 0; a < b; a++)
#define FORC(a,b,c) for(int a = b; a < c; a++)
#define OOB(a,b) (a < 0 || a > b)

int main() {
	int scenarios = 0;
	SCI(scenarios);
	FOR(s, scenarios){
		int deceit, regular, numblocks, nh,nl,kh,kl;
		deceit = 0;
		regular = 0;
		SCI(numblocks);
		kh = numblocks-1;
		nh = numblocks-1;
		kl = 0;
		nl = 0;
		double naomi[numblocks];
		double ken[numblocks];

		FOR(i, numblocks){
			assert(scanf("%lf", &naomi[i]));
		}
		FOR(i,numblocks){
			assert(scanf("%lf", &ken[i]));
		}

		sort(naomi, naomi+numblocks);
		sort(ken, ken+numblocks);


		if (naomi[nh] < ken[kl]){
			deceit = 0;
			regular = 0;
		} else if (naomi[nl] > ken[kh]){
			deceit = numblocks;
			regular = numblocks;
		} else {
		//deceit
			FOR(i, numblocks){
				if (naomi[nh] > ken[kh]){ 
					deceit++;
					nh--;
					kh--;
				} else { // Sacrifice lower.
					nl++;
					kh--;
				}
			}

			nl = 0;
			kl = 0;
			nh = numblocks-1;
			kh = numblocks-1;
		//regular
			FOR(i, numblocks){
				if (naomi[nh] > ken[kh]){ // Sacrifice kenlow.
					regular++;
					nh--;
					kl++;
				} else {
					nh--;
					kh--;
				}
			}
		}
		printf("Case #%d: %d %d\n",s+1, deceit, regular);
	}
	return 0;
}