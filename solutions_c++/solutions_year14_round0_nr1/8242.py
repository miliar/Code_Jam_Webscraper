#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

set<int> get() {
	int row;
	scanf("%d", &row);
	set<int> S;
	row--;
	int a, b, c, d;
	for(int i = 0; i < 4; i++) {
		scanf("%d%d%d%d", &a, &b, &c, &d);
		if(i == row) {
			S.insert(a);
			S.insert(b);
			S.insert(c);
			S.insert(d);
		}
	}
	return S;
}

int main() {
	int tests;
	scanf("%d", &tests);
	for(int test = 0; test < tests; test++) {
		set<int> A = get();
		set<int> B = get();
		vector<int> c(17);
		set_intersection(A.begin(), A.end(), B.begin(), B.end(), c.begin());
		printf("Case #%d: ", test + 1);
		int s = 0;
		while(c[s] != 0) s++;
		if(s == 0)
			printf("Volunteer cheated!\n");
		else if(s == 1)
			printf("%d\n", *(c.begin()));
		else
			printf("Bad magician!\n");
	}
	return 0;
}
