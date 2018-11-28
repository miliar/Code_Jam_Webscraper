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

int n;

string f(int i, string & s, bool type) {
	if(i == n) return s;
	if(s[i] == '?') {
		if(type) s[i] = '0';
		else s[i] = '9';
	}
	return f(i+1, s, type);
}

char sl[2][nax];

void te() {
	REP(i,2) scanf("%s", sl[i]);
	n = strlen(sl[0]);
	assert(n == (int) strlen(sl[1]));
	vector<ll> ANS;
	FOR(pref, 0, n-1) {
		
		{
			char old_a = sl[0][pref];
			char old_b = sl[1][pref];
			for(char a = '0'; a <= '9'; ++a)
				if(old_a == '?' || old_a == a)
					for(char b = '0'; b <= '9'; ++b)
						if(old_b == '?' || old_b == b) {
							string one = string(sl[0]);
							string two = string(sl[1]);
							one[pref] = a;
							two[pref] = b;
							REP(t1, 2) REP(t2, 2) {
								string memo[2] = {one, two};
								ll ans1 = stoll(f(pref+1, one, t1));
								ll ans2 = stoll(f(pref+1, two, t2));
								one = memo[0]; two = memo[1];
								vector<ll> maybe = vector<ll>{abs(ans1-ans2), ans1, ans2};
								if(ANS.empty() || maybe < ANS)
									ANS = maybe;
							}
							
						}
			sl[0][pref] = old_a;
			sl[1][pref] = old_b;
		}
		
		//if(pref == n) break;
		char & a = sl[0][pref];
		char & b = sl[1][pref];
		if(a == b) {
			if(a == '?') {
				a = b = '0';
			}
		}
		else if(a == '?') a = b;
		else if(b == '?') b = a;
		else break;
	}
	RI(i, 2) {
		ll x = ANS[i];
		vector<int> w;
		while(x) {
			w.pb(x % 10);
			x /= 10;
		}
		while((int) w.size() < n) w.pb(0);
		reverse(w.begin(), w.end());
		for(int dig : w) printf("%d", dig);
		printf(" ");
	}
	puts("");
	//printf("%lld %lld\n", ANS[1], ANS[2]);
}

int main() {
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
