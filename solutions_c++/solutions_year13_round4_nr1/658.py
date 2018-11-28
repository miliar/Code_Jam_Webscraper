#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "A"

struct Event {
	int64 type;
    int64 num;
    int64 th;
    int64 oth;
};

inline bool cmpfn(Event a, Event b) {
	if (a.th != b.th) return a.th < b.th;
	if (a.type != b.type) return a.type < b.type;
	return true;
}


const int MAXM = 10100;

const int64 MOD = 1000002013ll;

vector<Event> es;
pair <int64, pair <int64, int64> > res[MAXM];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);

        int n, m;
        scanf("%d %d", &n, &m);
        
        int64 need = 0;

        es.clear();

        for (int i = 0; i < m; i++) {
        	int64 o, e, k;
        	scanf("%I64d %I64d %I64d", &o, &e, &k);
        	Event in;
        	in.type = 0;
        	in.num = k;
        	in.th = o;
        	in.oth = e;
        	es.PB(in);

        	Event out;
        	out.type = 1;
        	out.num = k;
        	out.th = e;
        	out.oth = o;
        	es.PB(out);

        	int64 d = e - o;
        	int64 cneed = (d * (d-1) / 2) % MOD;
        	int64 aneed = (cneed * k) % MOD;
        	assert(aneed >= 0);
			need = (need + aneed) % MOD;
        }

        stable_sort(es.begin(), es.end(), cmpfn);

        int64 actual = 0;
        int last = 0;

        for (int ec = 0; ec < es.size(); ec++) {
        	Event e = es[ec];

        	//cerr << e.type << " " << e.th << " " << e.oth << " " << e.num << endl;
        	if (e.type == 0) {
        		last++;
        		res[last] = MP(e.num, MP(e.th, e.oth));
        	}
        	else {
        		int num = e.num;
        		
        		while (num > 0) {
        			assert(last > 0);

        			if (res[last].first > num) {
		        		int64 d = (e.th - res[last].second.first);
        				int64 paid = (d * (d-1) / 2) % MOD;
        				int64 apaid = (num * paid) % MOD;
        				actual = (actual + apaid) % MOD;
        				res[last].first -= num;
        				num = 0;
        			}
        			else {
        				int64 d = (e.th - res[last].second.first);
        				int64 paid = (d * (d-1) / 2) % MOD;
        				int64 apaid = (res[last].first * paid) % MOD;
        				actual = (actual + apaid) % MOD;
        				num -= res[last].first;
        				last--;
        			}
        		}
        	}
        }

        assert(last == 0);
		
		assert(need >= 0);

		assert(actual >= 0);
		

		printf("%I64d", (actual - need + MOD) % MOD);
        printf("\n");
    }

    return 0;
}
