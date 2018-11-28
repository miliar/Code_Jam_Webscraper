#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

 typedef long long ll;

set<int> getDigs(ll k) {
set<int> ret;
if(k == 0)  ret.insert(0);
else {
 while(k) {
ret.insert(k % 10);
k/= 10;
}
}
return ret;
}

int main() {
int T;
scanf("%d", &T);
for(int t = 1; t <= T; ++t) {
printf("Case #%d: ", t);
  ll n;
  scanf("%lld", &n);
  if(!n) puts("INSOMNIA");
else {
set<int> digs;
digs.clear();
ll k = 0;
do {
k += n;
set<int> curD = getDigs(k);
digs.insert(curD.begin(), curD.end());
} while((int) digs.size() != 10);
printf("%lld\n", k);
}
}


 return 0;
}
