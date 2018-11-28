#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <string>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>

#include <functional>
#include <limits>
#include <numeric>
#include <complex>

#include <cassert>
#include <cmath>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

template<typename X> inline X abs(const X& a) { return (a < 0 ? -a : a); }
template<typename X> inline X sqr(const X& a) { return (a * a); }

typedef long long li;
typedef long double ld;
typedef pair<int,int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned long long uli;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define fore(i, a, b) for(int i = int(a); i <= int(b); i++)
#define ford(i, n) for(int i = int(n - 1); i >= 0; i--)
#define foreach(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)

#define pb push_back
#define mp make_pair
#define mset(a, val) memset(a, val, sizeof (a))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define ft first
#define sc second
#define sz(a) int((a).size())

const int INF = int(1e9);
const li INF64 = li(INF) * li(INF);
const ld EPS = 1e-9;
const ld PI = ld(3.1415926535897932384626433832795);
double a[100009],b[100009];
int n;
bool done[100009];
int main()
{
    int cs=0,t,j,k,l,ans1,ans2;
    fstream F;
    F.open("input.in");
    freopen("o.txt","w",stdout);
    F>>t;
    while(t--) {
               F>>n;
               ans1=ans2=0;
               mset(done, 0);
               forn(i, n) F>>a[i];
               forn(i, n) F>>b[i];
               sort(a, a+n);
               sort(b, b+n);
               j=0;      
               k=n-1;
               l=0;
               ford(i, n) {
                       if(b[i]<a[k]) {
                                     j++;
                                     k--;
                                     }
                       }
               ans1 = j;
               j=0;
               k=0;
               for(j = 0; j < n; j++) {
                     for(k = 0; k < n; k++) {
                           if(done[k] == 0 && a[j] < b[k]) {
                                      done[k]=1;
                                      ans2++;
                                      break;
                                      }
                           }
               }
               ans2 = n - ans2;
               printf("Case #%d: %d %d\n",++cs,ans1,ans2);
    }
    return 0;
}
                                      
                                      
               
                                     
    
