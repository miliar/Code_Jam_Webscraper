#include <bits/stdc++.h>

using namespace std;
const int MOD = 1000000007;

class party {
public:
	int count, name;
	party(int count, int name) {
		this->count = count;
		this->name = name;
	}

	bool operator<(party b) const {
		return this->count < b.count;
	}
};

vector<party> p;
vector< pair<int, int> > final;
int n;
int exhaust(int sum, vector< pair<int, int> > answer) {

	if (sum<=0){
		final = answer;
		return 0;
	}

	for (int i = 0; i < n; i++) {
		if (p[i].count > sum / 2) {
			return 1;
		}
	}
	for (int i = 0; i < n; i++) {
		if (p[i].count > 0) {
			p[i].count -= 1;
			answer.push_back(pair<int,int>(p[i].name, -1));
			if (exhaust(sum - 1, answer) == 0) return 0;
			answer.pop_back();
			p[i].count += 1;
		}

		if (p[i].count >= 2) {
			p[i].count -= 2;
			answer.push_back(pair<int,int>(p[i].name, p[i].name));
			if (exhaust(sum - 2, answer) == 0) return 0;
			answer.pop_back();
			p[i].count += 2;
		}

		for (int j = i + 1; j < n; j++) {
			if (p[i].count >= 1 && p[j].count >= 1) {
				p[i].count -= 1;
				p[j].count -= 1;
				answer.push_back(pair<int,int>(p[i].name, p[j].name));
				if (exhaust(sum - 2, answer) == 0) return 0;
				answer.pop_back();
				p[i].count += 1;
				p[j].count += 1;
			}
		}
	}
	return 1;
}


int main() {
	int t, x, sum;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {

		p.clear();
		final.clear();
		cin >> n;
		sum = 0;
		for (int i = 0; i < n; i++) {
			cin >> x;
			p.push_back(party(x, i));
			sum += x;
		}

		sort(p.begin(), p.end());
		printf("Case #%d: ", tc);
		exhaust(sum, vector< pair<int, int> >());
		for (int i = 0; i < final.size(); i++) {
			printf("%c", final[i].first+'A');
			if (final[i].second != -1)
			printf("%c", final[i].second+'A');
			printf(" ");
		}
		printf("\n");
	}
}