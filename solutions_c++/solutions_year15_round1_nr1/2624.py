#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define ms0(x) memset((x),0,sizeof(x))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main(){
    freopen("/Users/hao/Dropbox/chmffwn1/gcj/Round1_2015/A-large.in", "r", stdin);
    freopen("/Users/hao/Dropbox/chmffwn1/gcj/Round1_2015/A-large.out", "w", stdout);
    ll T, N;
    cin >> T;
    rep(i, 0, T) {
        cin >> N;
        vector<ll> st;
        st.resize(N);
        ll re1 = 0, re2 = 0;
        ll maxInterval = 0;
        ll pos = 0;
        ll sumv = 0;
        rep(i, 0, N) {
            cin >> st[i];
            sumv += st[i];
            if ((i!=0) && (st[i] < st[i-1])) {
                re1 += st[i-1] - st[i];
                if ((st[i-1]-st[i]) >= maxInterval) {
                    maxInterval = st[i-1] - st[i];
                    pos = i - 1;
                }
            }
        }
        ll sp;
        rep(i, 0, N-1) {
            re2 += min(maxInterval, st[i]);
        }
        cout << "Case #" << (i+1) << ": " << re1 << " " << re2 << endl;
    }
	return 0;
}
