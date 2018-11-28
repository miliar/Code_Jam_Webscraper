#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <bitset>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <unordered_set>
#include <stack>
#include <algorithm>
#include <functional>
 
using namespace std;

#define MAX 1000008
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define mp make_pair
#define F first
#define S second
#define INF 0x3f3f3f3f
#define INT_MAX 2147483647
#define pb push_back
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define itr(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> lli;
typedef pair<int,pii> i3;
 
bool solve1(string s) {
    for(int i = 0; i < s.size(); i++) {
        if(s[i] != '+') return false;
    }
    return true;
}

string solve2(int x, string s) {
    for(int i = 0; i <= x; i++) {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    return s;
}
int main()
{
    read;
    write;
    int t; 
    gi(t);
    for(int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ": ";
        string s;
        cin >> s;
        int cnt = 0;
        int len = s.size() - 1;
        for(int i = len; i >= 0; i--) {
            if(solve1(s)) break;
            if(s[i] == '-') {
                s = solve2(i, s);
                cnt++;
            }
        }
        cout << cnt << endl;        
    } 
    return 0;
}