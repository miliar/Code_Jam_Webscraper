#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

int stupidSolution(){
    return 0;
}

void genTest(int n){
	freopen("input.txt", "wt", stdout);
    cout << n << endl;
    
    for (int i = 0; i < n; i++){
        
    }
}

struct point {
    long long x;
    bool ends;
    int i;
};

const int SIZE = 1000;

long long p[SIZE];
long long r[SIZE];

const long long mod = 1000002013;

bool cmp(point a, point b) {
    if (a.x == b.x) {
        return a.ends < b.ends;
    }
    return a.x < b.x;
}

long long f(long long from, long long to, long long cnt, long long n) {
    if (from == to) {
        return 0;
    }
    long long len = to - from;
    long long res = (((n + 1 - len + n) * len) / 2) % mod;
    return (res * cnt) % mod;
}

int main(){
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    
	int T;
	cin >> T;
    
	for (int t = 0; t < T; t++){
		int n, m;
        cin >> n >> m;
        
        long long nn = n;
        
        vector<point> v;
        
        long long sum1 = 0;
        
        for (int i = 0; i < m; i++) {
            long long o, e;
            cin >> o >> e >> p[i];
            r[i] = p[i];
            
            point pp;
            pp.i = i;
            
            pp.x = o;
            pp.ends = 0;
            v.push_back(pp);
            
            pp.x = e;
            pp.ends = 1;
            v.push_back(pp);
            
            sum1 = (sum1 + f(o, e, p[i], nn)) % mod;
        }
        
        sort(v.begin(), v.end(), cmp);
        
        set<pair<long long, int>> st;
        long long sum2 = 0;
        
        for (int i = 0; i < (int)v.size(); i++) {
            if (v[i].ends == 1) {
                long long cnt = p[v[i].i];
                long long curx = v[i].x;
                
                while (cnt > 0) {
                    int ind = st.begin()->second;
                    long long prevx = - st.begin()->first;
                    st.erase(st.begin());
                    
                    long long curcnt = min(cnt, r[ind]);
                    sum2 = (sum2 + f(prevx, curx, curcnt, nn)) % mod;
                    
                    cnt -= curcnt;
                    r[ind] -= curcnt;
                    if (r[ind] > 0) {
                        st.insert(make_pair(- prevx, ind));
                    }
                }
            }
            else {
                st.insert(make_pair(- v[i].x, v[i].i));
            }
        }
        
		cout << "Case #" << t + 1 << ": ";
		
        cout << (mod + (sum1 - sum2) % mod) % mod;
        
		cout << endl;
	}
}











