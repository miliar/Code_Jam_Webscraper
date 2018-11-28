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

string wzo[10];
bool vis[10];
char sl[nax];
int cnt[26];

void te() {
	REP(i, 10) vis[i] = false;
	scanf("%s", sl);
	int n = strlen(sl);
	REP(i, 26) cnt[i] = 0;
	REP(i, n) ++cnt[sl[i]-'A'];
	vi w;
	REP(_, 2) {
		for(char znak = 'A'; znak <= 'Z'; ++znak) {
			int which = -1;
			REP(i, 10) if(!vis[i]) {
				bool has = false;
				for(char a : wzo[i]) if(a == znak) has = true;
				if(has && which != -1) which = 100;
				if(has && which == -1) which = i;
			}
			if(which != -1 && which != 100) {
				while(cnt[znak-'A']) {
					for(char a : wzo[which])
						--cnt[a-'A'];
					w.pb(which);
				}
				//printf("%d(%c) ", which, znak);
				vis[which] = true;
			}
		}
	}
	sort(w.begin(), w.end());
	for(int x : w) printf("%d", x);
	puts("");
}

int main() {
	wzo[0] = "ZERO";
	wzo[1] = "ONE";
	wzo[2] = "TWO";
	wzo[3] = "THREE";
	wzo[4] = "FOUR";
	wzo[5] = "FIVE";
	wzo[6] = "SIX";
	wzo[7] = "SEVEN";
	wzo[8] = "EIGHT";
	wzo[9] = "NINE";
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
