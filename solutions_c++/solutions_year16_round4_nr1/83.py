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

map<pair<vi,int>, string> m;

string rec(vi three, int which) {
	int total = three[0] + three[1] + three[2];
	assert(total >= 1);
	if(total == 1) {
		if(three[which] == 1) {
			if(which == 0) return "R";
			if(which == 1) return "P";
			if(which == 2) return "S";
			assert(false);
		}
		return "";
	}
	assert(total > 1);
	assert(total % 2 == 0);
	auto para = mp(three, which);
	if(m.count(para)) return m[para];
	string ans = "";
	int about = total / 6;
	int low = max(0, about - 2);
	int high = about + 2;
	FOR(i, low, min(high, three[0]))
		FOR(j, low, min(high, three[1]))
			FOR(k, low, min(high, three[2])) {
		if(2 * (i + j + k) != total) continue;
		if(abs(i-j) > 1 || abs(i-k) > 1 || abs(j-k) > 1) continue;
	//FOR(i, max(0, about - magic))
	//FOR(i,0,three[0]) FOR(j,0,three[1]) {
	//	int k = total / 2 - i - j;
		vi a = vi{i,j,k};
		vi b = vi{three[0]-i, three[1]-j, three[2]-k};
		bool ok = true;
		for(int x : b) for(int y : b) if(abs(x-y) > 1) ok = false;
		if(!ok) continue;
		
		int which_loss = (which + 2) % 3;
		
		string one = rec(a, which);
		string two = rec(b, which_loss);
		
		if(!one.empty() && !two.empty()) {
			if(ans.empty() || ans > (one+two))
				ans = one + two;
			if(ans.empty() || ans > (two + one))
				ans = two + one;
		}
	}
	m[para] = ans;
	return ans;
}

void te() {
	int n, a, b, c;
	/*n = 1 << (rand() % 5);
	while(true) {
		a = rand() % n;
		b = rand() % n;
		c = rand() % n + 1;
		if(a + b + c == n)
			break;
	}*/
	scanf("%d%d%d%d", &n, &a, &b, &c);
	string ans;
	REP(i, 3) {
		string maybe = rec(vi{a,b,c}, i);
		// cout << maybe << " ";
		if(!maybe.empty())
			if(ans.empty() || ans > maybe)
				ans = maybe;
	}
	
	// if(!ans.empty()) printf("%d %d %d\n", a, b, c);
	const int K = 2;
	if(abs(a-b) >= K || abs(a-c) >= K || abs(b-c) >= K)
		assert(ans.empty());
	if(ans.empty()) ans = "IMPOSSIBLE";
	printf("%s\n", ans.c_str());
}

int main() {
	int T;
	scanf("%d", &T);
	RI(nr, T) {
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
