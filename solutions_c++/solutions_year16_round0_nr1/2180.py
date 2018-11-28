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

int ilosc, n, test;
bool bylo[100];

void dodaj(int c) {
  if (!bylo[c]) ++ilosc;
  bylo[c] = true;
}

void badaj(int x) {
  while (x) {
    dodaj(x%10);
    x /= 10;
  }
}

void solve() {
  scanf("%d",&n);
  if (n == 0) {
    puts("INSOMNIA");
    return;
  }
  
  int res = n;
  REP(i,10) bylo[i] = false;
  ilosc = 0;
  badaj(res);
  
  while (ilosc != 10) {
    res += n;
    badaj(res);
  } 
  
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
