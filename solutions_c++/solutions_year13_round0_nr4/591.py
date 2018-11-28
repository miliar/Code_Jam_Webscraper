
#include <map>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define foreach(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

int startWith(int openChestsSet, int initialKeysCount, int chestsCount, vector<int> &initialKeys,
		 vector<int> &openWith, vector<vector<int> > &insideChest, vector<int> &cache) {
	if (openChestsSet == (1 << chestsCount) - 1) {
		return chestsCount + 1;
	} else if (cache[openChestsSet] != -1) {
		return cache[openChestsSet];
	} else {
		map<int, int> keyCounts;
		foreach (it, initialKeys)
			keyCounts[*it]++;
		for (int chest = 0; chest < chestsCount; ++chest)
			if ((openChestsSet & (1 << chest)) != 0) {
				keyCounts[openWith[chest]]--;
				foreach (it, insideChest[chest])
					keyCounts[*it]++;
			}
		for (int chest = 0; chest < chestsCount; ++chest)
			if ((openChestsSet & (1 << chest)) == 0 
					&& keyCounts.count(openWith[chest]) 
					&& keyCounts[openWith[chest]] > 0) {
				int res = startWith(openChestsSet | (1 << chest), initialKeysCount, chestsCount,
					initialKeys, openWith, insideChest, cache);
				if (res >= 0)
					return cache[openChestsSet] = chest;
			}
		return cache[openChestsSet] = -2;
	}
}

int main() {
	int tst = nextInt();
	for (int cas = 0; cas < tst; ++cas) {
		int initialKeysCount = nextInt();
		int chestsCount = nextInt();
		vector<int> initialKeys;
		for (int key = 0; key < initialKeysCount; ++key) {
			initialKeys.push_back(nextInt());
		}
		vector<int> openWith(chestsCount);
		vector<vector<int> > insideChest(chestsCount, vector<int>());
		for (int c = 0; c < chestsCount; ++c) {
			openWith[c] = nextInt();
			int keysCount = nextInt();
			for (int key = 0; key < keysCount; ++key)
				insideChest[c].push_back(nextInt());
		}
		vector<int> cache(1 << chestsCount, -1);
		if (startWith(0, initialKeysCount, chestsCount, initialKeys, openWith, insideChest, cache) < 0) {
			printf("Case #%d: IMPOSSIBLE\n", cas + 1);
		} else {
			int set = 0;
			printf("Case #%d:", cas + 1);
			while (set != (1 << chestsCount) - 1) {
				printf(" %d", cache[set] + 1);
				set |= 1 << cache[set];
			}
			puts("");
		}
	}
	return 0;
}