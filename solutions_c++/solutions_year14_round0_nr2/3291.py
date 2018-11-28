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

#define CPS 2;

int main() {
	int scenarios = 0;
	SCI(scenarios);
	FOR(s, scenarios){
		double best, current;
		double farmcost, farmcps, goal, currentcps, temp;
		bool found = false;
		assert(scanf("%lf %lf %lf", &farmcost, &farmcps, &goal) > 0);
		best = goal/CPS;
		current = farmcost/CPS;
		currentcps = CPS;
		while(true){
			temp = current + goal/(currentcps + farmcps);
			if (temp > best){
				break;
			} else {
				best = temp;
				currentcps += farmcps;
				current += farmcost/(currentcps);
			}
		}
		printf("Case #%d: %0.7f\n", s+1, best);
	}	
	return 0;
}