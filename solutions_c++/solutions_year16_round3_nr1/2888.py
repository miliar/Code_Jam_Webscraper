#include <bits/stdc++.h>

using namespace std;

set<pair<int, char> > st;

int main(void) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n;
		scanf("%d", &n);


		long long sm = 0;
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			sm += x;
			st.insert(make_pair(x, 'A' + i));
		}

		printf("Case #%d: ", i);

		while (1) {
			auto x = --st.end();
			st.erase(x);

			pair<int, char> p1, p2;
			p1 = *x;

			if (p1.first == 0) break;
			p1.first -= 1;
			--sm;
			st.insert(p1);

			auto y = --st.end();
			st.erase(y);

			p2 = * y;
			if (p2.first == 0) {
				printf("%c", p1.second);
				break;
			}
			p2.first -= 1;
			st.insert(p2);
			--sm;

			auto z = --st.end();

			if (2 * (*z).first > sm) {
				printf("%c ", p1.second);
				st.erase(p2);
				p2.first += 1;
				sm += 1;
				st.insert(p2);
			}
			else {
				printf("%c", p1.second);
				printf("%c ", p2.second);
			}

		}
		printf("\n");
	}
}