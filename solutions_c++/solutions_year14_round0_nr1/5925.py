#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

vector<int> r;
map<int, int> m;

int main() {
	freopen("input.in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		int n;
		m.clear();
		r.clear();
		scanf("%d", &n);
		n--;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int x;
				scanf("%d", &x);
				if(i == n) m[x]++;
			}
		}
		scanf("%d", &n);
		n--;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int x;
				scanf("%d", &x);
				if(i == n) m[x]++;
			}
		}
		map<int, int>::iterator it;
		for(it = m.begin(); it != m.end(); it++) {
			if((*it).second == 2) {
				r.push_back((*it).first);
			}
		}
		printf("Case #%d: ", test);
		if(r.size() == 0) {
			printf("Volunteer cheated!\n");
		}
		else if(r.size() == 1) {
			printf("%d\n", r[0]);
		}
		else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
			
		
