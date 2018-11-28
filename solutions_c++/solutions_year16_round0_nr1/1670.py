#include <bits/stdc++.h>

using namespace std;

int TC, N, num;
bool sleep;
set<char> seen;

void updateSeen(int num) {
	stringstream out;
	out << num;
	string s = out.str();
	for (int i = 0; i < s.length(); i++) {
		seen.insert(s[i]);
	}
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d", &N);
		seen.clear(); sleep = false; num = N;
		for (int i = 1; i <= 100; i++) {
			num = N*i;
			updateSeen(num);
			if (seen.size() == 10) {
				printf("Case #%d: %d\n", tc, num);
				sleep = true;
				break;
			}
		}
		if (!sleep) printf("Case #%d: INSOMNIA\n", tc);
	}
	return 0;
}