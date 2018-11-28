#include <cstdio>
#include <set>
#include <algorithm>
#include <iterator>

int main() {
	using namespace std;
	set<int> first;
	set<int> second;
	set<int> intersect;
	int temp[4];
	int T;
	int row;
	
	scanf("%d", &T);
	for (int i=0; i<T; ++i) {
		scanf("%d", &row);
		for (int j=0; j<4; ++j) {
			scanf("%d %d %d %d", &temp[0], &temp[1], &temp[2], &temp[3]);
			if (row == (j+1)) {
				first.insert(temp[0]);
				first.insert(temp[1]);
				first.insert(temp[2]);
				first.insert(temp[3]);
			}
		}
		scanf("%d", &row);
		for (int j=0; j<4; ++j) {
			scanf("%d %d %d %d", &temp[0], &temp[1], &temp[2], &temp[3]);
			if (row == (j+1)) {
				second.insert(temp[0]);
				second.insert(temp[1]);
				second.insert(temp[2]);
				second.insert(temp[3]);
			}
		}
		
		set_intersection(first.begin(), first.end(), second.begin(), second.end(), inserter(intersect, intersect.begin()));
		if (intersect.size() == 0) {
			printf("Case #%d: Volunteer cheated!\n", i+1);
		} else if (intersect.size() == 1) {
			printf("Case #%d: %d\n", i+1, *intersect.begin());
		} else {
			printf("Case #%d: Bad magician!\n", i+1);
		}
		
		first.clear();
		second.clear();
		intersect.clear();
	}
	
}