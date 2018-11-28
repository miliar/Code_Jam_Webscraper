
#define _USE_MATH_DEFINES

#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

#define D(var) { cout << #var << ": " << (var) << endl; }
template <class T> ostream& operator << (ostream &os, const vector<T> &temp) { os << "[ "; for (unsigned int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const set<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const multiset<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const pair<S,T> &a) { os << "(" << a.first << "," << a.second << ")"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const map<S,T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (it->first) << "->" << it->second; os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const deque<T> &temp) { os << "[ "; for (int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)

typedef long long ll;

ll nc(string &s) {
    ll m=0;
    ll c=0;
    for(ll i=0;i<s.size();i++) {
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') {
            c=0;
            continue;
        } else {
            ++c;
            m = max(c,m);
        }
    }
    //D(m);
    return m;
}

ll solve()
{
    string s;
    ll n;
    ll c=0;
    cin >> s >> n;
    for(ll i=0;i<s.size();i++) {
        for(ll j=1;j<=s.size()-i;j++) {
            string subs=s.substr(i,j);
            
            if(nc(subs)>=n) {
                //D(subs);
                c++;
            }
        }
    }
    return c;
}

int main(int argc, const char * argv[])
{
    freopen("small1.in", "r", stdin);
    freopen("small1.out","w", stdout);
    
    int T; cin >> T;
    for (int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": "  << solve() << endl;
    }
    return 0;
}

