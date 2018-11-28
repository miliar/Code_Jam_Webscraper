#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>

#include <cstring>
#include <cstdio>
#include <memory.h>
#include <ctime>
#include <cassert>
#include <cmath>
#include <iomanip>

#define eps e-8

using namespace std;
#define forn(i,n) for(int i = 0; i < int(n); i++)
//#define ford(i,n) for(int i = int(n) - 1; i >= 0; i--)
//#define fore(i,a,b) for(int i = int(a); i <= int(b); i++)
//
//#define foreach(it,a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
//#define mp make_pair
//#define pb push_back
//#define L(s) ((int)((s).size()))
//#define sq(x) ((x)*(x))
//
//#define sign(x) ( ((x) > 0) ? 1 : -1)
#define ll long long
//#define INF 1000000000
//
//#define MAXN 100010

void solve() {
    int T;
    cin>>T;
    for(int t=0; t<T; ++t){
        int n;
        cin>>n;
        string s;
        cin>>s;
        int res=0;
        int cur=0;
        for(int j=0; j<s.size(); ++j){
            int p=s[j]-'0';
            int add=max(j-cur, 0);
            cur+=p+add;
            res+=add;
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
}


int main()
{
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
#ifdef diametralis
    freopen("/Users/diametralis/Documents/projects/IO/input.txt", "rt", stdin);
    freopen("/Users/diametralis/Documents/projects/IO/output.txt", "wt", stdout);
#endif
    solve();
#ifdef diametralis
    cerr << "Time == " << clock() << endl;
#endif
}