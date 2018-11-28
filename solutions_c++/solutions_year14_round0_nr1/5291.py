#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		set<int> cards;
		FOR(i, 1, 16) cards.insert(i);
		REP(guess, 2) {
			int row;	
			cin >> row;
			FOR(r, 1, 4)
			FOR(j, 1, 4) {
				int x;
				cin >> x;
				if (r != row) cards.erase(x);
			}
		}
		printf("Case #%d: ", cN);
		if (cards.size() == 0) puts("Volunteer cheated!");
		else if (cards.size() > 1) puts("Bad magician!");
		else printf("%d\n", *cards.begin());
	}
}
