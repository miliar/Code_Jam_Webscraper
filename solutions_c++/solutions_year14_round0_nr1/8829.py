#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int main() {
	int tt, a1, a2, tmp;
	set<int> s;
	
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++) {
		s.clear();
		scanf("%d", &a1);
		for (int i = 1; i<=4; i++)
			for (int j = 0; j<4; j++) {
				scanf("%d", &tmp);
				if (i == a1)
					s.insert(tmp);
			}
		scanf("%d", &a2);
		int found = 0;
		int first = -1;
		for (int i = 1; i<=4; i++)
			for (int j = 0; j<4; j++) {
				scanf("%d", &tmp);
				if (i == a2 && s.find(tmp) != s.end()) {
					found++;
					first = tmp;
				}
			}
		if (found == 1) 
			printf("Case #%d: %d\n", t, first);
		else if (found == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else if (found > 1)
			printf("Case #%d: Bad magician!\n", t);
	}
	// your code goes here
	return 0;
}