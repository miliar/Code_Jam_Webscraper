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
int main()
{
    fstream F;
    F.open("input.in");
    freopen("o.txt","w",stdout);
    int t;
    int r1,r2,a[4][4],b[4][4],j,k,m[4],n[4],ans,num;
    F>>t;
    for(int i=1; i<=t;i++) {
            ans=0;
            F>>r1;
            for(j=0;j<4;j++) for(k=0;k<4;k++) F>>a[j][k];
            for(j=0;j<4;j++) m[j]=a[r1-1][j];
            F>>r2;
            for(j=0;j<4;j++) for(k=0;k<4;k++) F>>b[j][k];
            for(j=0;j<4;j++) n[j]=b[r2-1][j];
            //sort(m,m+4);
            //sort(n,n+4);
            
            for(j=0;j<4;j++) {
                             for(k=0;k<4;k++){
                                              if(m[j] == n[k]) {
                                     ans++;
                                     num=m[j];
                                     }
                                     }}
            if(ans == 1) {
                   printf("Case #%d: %d\n",i,num);
                   }
            else if(ans ==0) {
                 printf("Case #%d: Volunteer cheated!\n",i);
                 }
            else {
                 printf("Case #%d: Bad magician!\n",i);
                 }
            }
    return 0;
}
                 
                                     
            
    
    
