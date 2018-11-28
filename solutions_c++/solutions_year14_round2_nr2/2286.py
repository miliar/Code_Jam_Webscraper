#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long double ld;

FILE * fin, *fout;

int bitCount(ll n) {
	ll t = 1ll;
	int cnt = 0;
	while(t < n) {
		cnt++;
		t = t << 1ll;
	}
	return cnt;
}

void solve(int problemIdx) {
	ll a, b, k;
	// read
	fscanf(fin, "%lld %lld %lld", &a, &b, &k);
	
	ll win = 0ll;
	int la = bitCount(a);
	int lb = bitCount(b);
	ll mask = ((1ll << la) - 1ll) & ((1ll << lb) - 1ll);
	
	printf("problem: %d\nla=%d lb=%d mask=%lld\n", problemIdx, la, lb, mask);
	
	for(ll i = 0ll; i<a; i++) {
		for(ll j=0ll; j<b; j++) {
			if((i & j) < k) {
				//printf("%lld %lld\n", i, j);
				win++;
			}
		}
	}
	
	// output
	fprintf(fout, "Case #%d: %lld\n", problemIdx, win);
}

int main(int argc, char** argv) {
	fin = fopen("input.txt", "rt");
	fout = fopen("output.txt", "wt");
	if(NULL == fin || NULL == fout) {
		printf("error opening files...\n");
		return -1;
	}
	
	int nrProblems;
	fscanf(fin, "%d", &nrProblems);
	for(int problemIdx = 1; problemIdx <= nrProblems; problemIdx++) {
		solve(problemIdx);
	}
		
	return 0;
}