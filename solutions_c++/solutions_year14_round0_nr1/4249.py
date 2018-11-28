#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <bitset>
#include <algorithm>
#include <cstring>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define rtrav(it, v) for(typeof((v).rbegin()) it = (v).rbegin(); it != (v).rend(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(int argc, char const *argv[]) {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int R1, R2, tmp;
		set<int> s1, s2;
		scanf("%d", &R1);
		rep(r, 1, 5) {
			rep(c, 0, 4) {
				scanf("%d", &tmp);
				if (R1 == r) {
					s1.insert(tmp);
				}
			}
		}
		scanf("%d", &R2);
		rep(r, 1, 5) {
			rep(c, 0, 4) {
				scanf("%d", &tmp);
				if (R2 == r && s1.count(tmp)) {
					s2.insert(tmp);
				}
			}
		}
		printf("Case #%d: ", t+1);
		if (s2.size() == 0) printf("Volunteer cheated!\n");
		else if (s2.size() == 1) printf("%d\n",*s2.begin());
		else printf("Bad magician!\n");
	}
}