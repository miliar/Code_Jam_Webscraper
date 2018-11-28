#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "a.in" );
ofstream out( "a.out" );

void add(vi& head, vi& data, vi& next, int val, int idx) {
    next.push_back(head[val]);
    head[val] = data.size();
    data.push_back(idx);
}

int main() {
    int ntests;
    in >> ntests;    
    for (int test = 1; test <= ntests; ++test) {        
        int n, d;
        int s, as, cs, rs;
        int m, am, cm, rm;
        in >> n >> d;
        in >> s >> as >> cs >> rs;
        in >> m >> am >> cm >> rm;
        vi min_sal(n), max_sal(n), inside(n);

        //vi starts_head(rs, -1), starts, starts_next;
        //vi ends_head(rs, -1), ends, ends_next;
        vi head(rs, -1), ids, next;
        min_sal[0] = max_sal[0] = s;
        add(head, ids, next, s, 0);
        add(head, ids, next, s, 0);
        for (int i = 1; i < n; ++i) {
            s = (ll(s) * as + cs) % rs;
            m = (ll(m) * am + cm) % rm;
            int manager = m % i;            
            min_sal[i] = min(s, min_sal[manager]);
            max_sal[i] = max(s, max_sal[manager]);
            /*add(starts_head, starts, starts_next, min_sal[i], i);
            add(ends_head, ends, ends_next, max_sal[i], i);*/
            add(head, ids, next, min_sal[i], i);
            add(head, ids, next, max_sal[i], i);
        }
        int current = 0;
        int best = 0;
        for (int hi = 0; hi < rs; ++hi) {
            int lo = hi - d;
            for (int t = head[hi]; t != -1; t = next[t]) {
                int id = ids[t];
                inside[id]++;
                if (inside[id] == 2)
                    ++current;
            }
            if (lo <= min_sal[0] && min_sal[0] <= hi)
                best = max(best, current);
            if (lo < 0)
                continue;
            for (int t = head[lo]; t != -1; t = next[t]) {
                int id = ids[t];
                inside[id]--;
                if (inside[id] == 1)
                    --current;
            }
        }
        out << "Case #" << test << ": " << best << "\n";
    }
    return 0;
}