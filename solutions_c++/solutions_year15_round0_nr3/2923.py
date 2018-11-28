#include <cstdio>
#include <utility>
#include <vector>
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef pair<char, int> pi;

#define MP make_pair

pi mul(pi a, pi b) {
	if(a.FI == '1') {
		return MP(b.FI, a.SE* b.SE);	
	}
	if(a.FI == b.FI) {
		return MP('1', -a.SE * b.SE);
	}
	if(a.FI == 'i' && b.FI == 'j') {
		return MP('k', a.SE * b.SE);
	}
	if(a.FI == 'j' && b.FI == 'k') {
		return MP('i', a.SE * b.SE);
	}
	if(a.FI == 'k' && b.FI == 'i') {
		return MP('j', a.SE * b.SE);
	}
	if(a.FI == 'i' && b.FI == 'k') {
		return MP('j', -a.SE * b.SE);
	}
	if(a.FI == 'j' && b.FI == 'i') {
		return MP('k', -a.SE * b.SE);
	}
	if(a.FI == 'k' && b.FI == 'j') {
		return MP('i', -a.SE * b.SE);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <=t; ++i ) {
		int res = 1;
		pi current = MP('1', 1);
		int n, k;
		char c;
		scanf ("%d%d\n", &n, &k);
		vector<char> v;
		for (int j = 0; j < n; ++j) {
			c = getchar();
			v.PB(c);
		}
		getchar();

		while (k--) {
			for (int j = 0; j < n; ++j) {
				current = mul(current, MP(v[j], 1));
				if (current == MP('i', 1) && res == 1) {
					++res;
					current = MP('1', 1);
				} else if (current == MP('j', 1) && res == 2) {
					++res;
					current = MP('1', 1);
				}
				else if (current == MP('k', 1) && res == 3) {
					++res;
					current = MP('1', 1);
				}
			}
		}

//		printf("Wyn - %c %d\n", current.FI, current.SE);

		printf("Case #%d: %s\n", i, (current == MP('1', 1) && res == 4) ? "YES" : "NO");
	}
	return 0;
}