#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1e6 + 5;

int test;
char t[nax];

void solve() {
  scanf(" %s",t);
  int dl = strlen(t);
  
  int res = 0;
  FOR(i,1,dl-1) if (t[i] != t[i-1]) ++res;
  if (t[dl-1] == '-') ++res;
  printf("%d\n",res);
}

int main() {	
  scanf("%d",&test);
  FOR(g,1,test) {
    printf("Case #%d: ",g);
    solve();
  }
	return 0;
}
