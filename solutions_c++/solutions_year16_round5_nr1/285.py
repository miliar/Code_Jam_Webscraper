#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;
string s;

int main() {
    scanf("%d", &TC);

    for (int tc = 1; tc <= TC; ++tc) {
	printf("Case #%d: ", tc);
	cin >> s;
	int n = s.size();
	
	list<bool> v;
	rep(i, n) v.pb(s[i] == 'J');

	int nc = n / 2;

	while (true) {
	    if (v.size() < 2) break;

	    auto it = v.begin();
	    auto it2 = it;
	    it2++;

	    bool f = 0;

	    while (it2 != v.end()) {
		if (*it == *it2) {
		    v.erase(it);
		    v.erase(it2);
		    f = 1;
		    break;
		}
		++it2;
		++it;
	    }

	    if (!f) break;
	    ++nc;
	}

	printf("%d\n", nc * 5);
    }

    return 0;
}
