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
#define trav(it, v) for(auto it = (v).begin(); it != (v).end(); ++it)
#define rtrav(it, v) for(typeof((v).rbegin()) it = (v).rbegin(); it != (v).rend(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(int argc, char const *argv[]) {
	int T;
	scanf("%d", &T);
	rep(t, 0, T) {
		int N, X;
		scanf("%d%d",&N,&X);
		multiset<int> files;
		rep(n,0,N) {
			int tmp;
			scanf("%d",&tmp);
			files.insert(tmp);
		}

		int discs = 0;
		while(!files.empty()) {
			discs++;
			auto it = files.end(); --it;
			int s1 = *it; files.erase(it);
			int ds = X-s1;
//			printf("%d %d\n",s1,ds);
			it = files.lower_bound(ds);
			if (it != files.begin()) {
				if (it == files.end()) --it;
				while (it != files.begin() && *it > ds) --it;
			}
			if (it != files.end() && *it <= ds) files.erase(it);
		}
		printf("Case #%d: %d\n", t+1, discs);
	}
	return 0;
}