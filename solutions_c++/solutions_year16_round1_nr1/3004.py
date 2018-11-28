#include <cstdio>
#include <cstring>
#include <list>
#include <algorithm>
using namespace std;
char o[1011];
list<char> pu;
int main() {
	int i, t;
	int k = 0;
	int n;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		scanf("%s", o);
		printf("Case #%d: ", ++k);
		n = strlen(o);
		for (i = 0; i < n; i++) {
			if (!(pu.size())) pu.push_front(o[i]);
			else if (pu.front() > o[i]) pu.push_back(o[i]);
			else pu.push_front(o[i]);
		}
		while (pu.size()) {
			printf("%c", pu.front());
			pu.pop_front();
		}
		printf("\n");
	}
	return 0;
}