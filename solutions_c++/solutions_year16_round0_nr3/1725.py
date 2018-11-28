#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>
#define _ << " _ " <<
#define dbg(x) cerr << #x << " == " << x << endl
#define mp(x,y) make_pair((x),(y))
#define pv(x,y) {for(typeof(y) z=(x);z!=(y);z++)cerr<<*z<<" ";cerr<<endl;}
#define rep(x,y) for(int(x)=(0);(x)<int(y);++(x))
#define x first
#define y second
using namespace std;

typedef long long ll;
typedef pair<int,int> pt;

#if 0
#define GENERATE 1
#endif

int N, J;

void read() {
	cin >> N >> J;
}

int fmod(string& s, int base, int p) {
	int pot = 1, r = 0;
	for (int i = s.size()-1; i >= 0; i--) {
		if (s[i] == '1') {
			r = (r + pot) % p;
		}
		pot = (pot * base) % p;
	}
	return r;
}

vector<int> prime;

void pp() {
	for(int p=2;p<1<<15;p++) {
		int ok=1;
		for(int j=2;ok && j*j<=p;j++) ok=p%j;
		if(ok) prime.push_back(p);
	}
}

void process() {
	puts("");
	set<string> mark;
	for(int q=0;mark.size()<J && q < 1e9; q++) {
		string s;
		for(int i=0;i<N-2;i++) if(rand()&1) s+="1"; else s+="0";
		s = "1" + s + "1";
		//dbg(s);
		if(!mark.count(s)) {
			vector<int> ans;
			for(int base=2;base<=10;base++) {
				for(int i=0;i<prime.size(); i++) {
					int p = prime[i];
					if (fmod(s,base,p) == 0) {
						ans.push_back(p);
						break;
					}
				}
			}
			//dbg(ans.size());
			//pv(ans.begin(),ans.end());
			if(ans.size()==9) {
				mark.insert(s);
				printf("%s", s.c_str());
				for(int i=0;i<9;i++) printf(" %d", ans[i]);
				puts("");
			}
		}
	}

}

int main() {
	srand(4777);
	pp();
	int T;
#ifdef GENERATE
	unsigned int seed=time(0);
	dbg(seed);
	srand(seed);
	T=50;
	for(int testcase=1;testcase<=T;++testcase) {
		fprintf(stderr,"Case #%d:",testcase);
		// *generate input!
		// BEGIN
		// END
#else
		cin>>T;
		for(int testcase=1;testcase<=T;++testcase) {
			fprintf(stdout,"Case #%d:",testcase);
			read();
#endif
		try {
			process();
		} catch(char const*exception) {
			puts(exception);
		}
	}
	return 0;
}
