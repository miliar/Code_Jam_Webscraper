#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
 
#include <iostream>
#include <algorithm>
#include <string>
 
#include <vector>
#include <set>
#include <map>
#include <queue>
 
using namespace std;
 
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;
 
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})
 
int ar[17];
 
void solve() {
SET(ar, 0);
int k = SI - 1;
REP(i, 4)
REP(j, 4) {
int x = SI;
if(i == k) ar[x] = 1;
}
int cnt = 0, ans;
k = SI - 1;
REP(i, 4)
REP(j, 4) {
int x = SI;
if(i == k && ar[x]) {
cnt++;
ans = x;
}
}
 
if (cnt == 1)
printf("%d\n", ans);
else if (cnt == 0)
puts("Volunteer cheated!");
else
puts("Bad magician!");
}
 
int main() {
for(int kase = 1,kases = SI; kase <= kases; kase++) {
printf("Case #%d: ", kase);
solve();
}
return 0;
}