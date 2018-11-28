#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <exception>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <regex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <typeinfo>
#include <vector>

using namespace std;
template <typename T, size_t N> struct ma : array<T,N> { T& operator[](size_t n) {
#ifdef DEBUG
           assert(n < N);
#endif
return (*static_cast<array<T,N>*>(this))[n]; } } ; 

typedef long long ll; typedef long double ld; typedef vector<int> vi; typedef vector<string> vs; typedef ostringstream oss; typedef istringstream iss; 

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); } 
template<> string to_str<ld>(const ld& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); } 
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
#define rep(i,b) for(auto i=(0);i<(b);++i)
#define fo(i,a,b) for(auto i=(a);i<=(b);++i)
#define ford(i,a,b) for(auto i=(a);i>=(b);--i)
#define fore(a,b) for(auto &a:(b))
#define v vector
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))


int cond = (ll)1;
#define db(x...) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
#define dbv(x, a, b) { if (cond > 0) { cerr << __LINE__<<": " << #x << " "; for (auto __it = (x).begin() + (a); __it < (x).begin() + (b); __it++) cerr << *__it <<" "; cerr << endl; } cerr.flush(); }

template <class C, class=typename C::iterator> struct _cprint { }; 
template<> struct _cprint<string> {};
template <class C, class=typename _cprint<C>::type> ostream& operator<<(ostream &o, const C& v){ for(auto x:v) o<<x<<" "; return o; }

#define d2 array<int, 2>
void solve() { db(1);
    int N;
    cin>>N;
    vi dat(N);
    vector<d2> sor(N);
    rep (i, N) cin >> dat[i];
    rep (i, N) sor[i] = d2({{dat[i], i}});
    sort(all(sor));
    int res = 0;
    rep (i, N) {
        int mode = 0;
        d2 ar = {{0, 0}};
        for (int j = 0; j < N; j++) {
            if (sor[i][0] == dat[j]) {
                mode = 1;
            }
            else if (sor[i][0] < dat[j]) {
                ar[mode]++;
            }
        }
        db(i<<" "<<sor[i][0]);
        db(i<<" "<<sor[i][0]<<" "<<ar[0]<<" "<<ar[1]);
        res += min(ar[0], ar[1]);
    }
    cout << res;
}

void brute() {}
void gen() {}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);
    //  freopen("../1.in","r",stdin); 
    //  freopen("../2.in","r",stdin); 
    //  freopen("../3.in","r",stdin); 
    //  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
    //  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
    //  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
    //  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
    //  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout)

    cond = argc >= 2 && argv[1][0] == 'q' ? 1000 : 0;
    int t;
    cin>>t;
    for (int i = 1; i <= t; i++) {
        if (cond)
            cerr << __LINE__ << " " << i << endl;
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
        cout.flush();
        cerr.flush();
    }
	return 0;
}

