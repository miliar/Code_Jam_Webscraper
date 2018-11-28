#include <cstdio>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstring>
#include <bitset>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>

#define  each(v,c)  for(typeof((c).begin()) v = (c).begin(); v != (c).end(); ++v)
#define  sync(x)    ios_base::sync_with_stdio(x)
#define  sz(a)      ((int)(a.size()))
#define  all(a)     (a).begin(), (a).end()
#define  pb         push_back
#define  mp         make_pair
#define  fi         first
#define  se         second
using namespace std;

#define debug(a,n)    cerr << "["; for(int i = 0; i < n; ++i) cerr << a[i] << " ";cerr << "\b]\n";
#define dbg(args...)  {debug1,args; cerr<<endl;}
#define pause()       cin.get();cin.get();

struct debugger {
    template<typename T> debugger& operator , (const T& v) {
        cerr<<v<<" "; return *this;
    }
} debug1;

template <typename T1, typename T2>
inline ostream& operator << (ostream& os, const pair<T1, T2>& p) {
    return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
inline ostream &operator << (ostream & os,const vector<T>& v) {
    bool first = true; os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if(!first) os << ", ";
        os << *ii; first = false;
    }
    return os << "]";
}

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef vector<int> vi;
const int inf = 0x7fffffff;

long long fp(long long a,long long b){
    long long ans = 1LL;
    while(b > 0){
        if (b & 1)
            ans = (ans * a);
        a = (a*a);
        b >>= 1;
    }
    return ans;
}

void solve(int tc){
    long long k,c,s;
    cin >> k >> c >> s;

    long long add = fp(k,c-1);
    long long cur = 1LL;

    cout << "Case #" << tc << ": ";
    for(int i = 1; i <= k; ++i){
        cout << cur;
        if (i != k) cout << " ";
        else cout << "\n";
        cur += add;
    }
}

int main(int argc, char **argv)
{
    int tc;
    cin >> tc;
    for(int i = 1; i <= tc; ++i)
        solve(i);
    return 0;
}
