#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <string.h>
#include <bitset>
#include <set>

#define FOR(i, a,b) for(int i=int(a);i<int(b);i++)
#define foreach(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)


using namespace std;
int t;
int cases = 1;
void resolve() {
	int s;
	string sk;
	cin >> s >> sk;
	int cinit = sk[0] - '0';

	int res = 0;
	FOR(i, 1, sk.size()) {
		int subs = cinit - i;
		if(subs < 0) {
			res += abs(subs);
			cinit += abs(subs) +  (sk[i] - '0');
		} else {
			cinit += (sk[i] - '0');	
		}
		
	}
	cout << "Case #" << cases++ << ": " << res << endl;

}

int main(){
	cin >> t;
	FOR(i, 0, t) {
		resolve();
	}
}
