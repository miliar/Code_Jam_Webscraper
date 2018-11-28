#include <bits/stdc++.h>

using namespace std;

struct state {
	vector<int> cnt;
	vector<int> ret;
	int used;
};

vector<int> total;
int goal;

vector<int> resp;
bool found;

string numbers[10] = {
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX",
	"SEVEN",
	"EIGHT",
	"NINE"
};

void solve(state st, int i) {
	if (found) return;

	if (st.used == goal) {
		resp = st.ret;
		found = true;
		return;
	}

	for (int j = i; j < 10; j++) {
		state next = st;		
		bool valid = true;

		for (int c = 0; c < numbers[j].size(); c++) {
			if (st.cnt[numbers[j][c] - 'A'] == 0) {
				valid = false;
			} else {
				next.cnt[numbers[j][c] - 'A']--;
				next.used++;
			}
		}

		if (valid) {
			next.ret.push_back(j);

			solve(next, j);
		}
	}
}

int main() {
	int t;
	cin >> t;

	string s;
	for (int n = 1; n <= t; n++) {
		cin >> s;
		total.resize(26);
		resp.clear();
		
		for (int i = 0; i < 26; i++) {
			total[i] = 0;
		}

		goal = s.size();
		for (int i = 0; i < goal; i++) {
			total[s[i] - 'A'] += 1;
		}

		state init;
		init.used = 0;
		init.cnt = total;

		found = false;
		solve(init, 0);

		printf("Case #%d: ", n);
		for (int i = 0; i < resp.size(); i++) {
			printf("%d", resp[i]);
		}
		printf("\n");
	}
	return 0;
}