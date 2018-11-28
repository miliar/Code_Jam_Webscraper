#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

vector<int> cnt[100];

string process(string &s, vector<int> &cnt) {
	int c = 0;
	char ch = '\0';
	string model;

	for(int i = 0; i < s.size(); i++) {
		if(s[i] == ch) {
			c++;
		} else {
			cnt.push_back(c);
			model += s[i];

			ch = s[i];
			c = 1;
		}
	}

	cnt.push_back(c);

	return model;
}

int compute_ans(int N) {
	int ans = 0;

	for(int i = 0; i < cnt[0].size(); i++) {
		vector<int> v;
		for(int j = 0; j < N; j++) {
			v.push_back(cnt[j][i]);
		}

		sort(v.begin(), v.end());

		int median = v[N/2];

		for(int j = 0; j < N; j++) {
			ans += abs(median - v[j]);
		}
	}

	return ans;
}

void test() {
	int N;
	string model;
	bool nice = true;

	cin >> N;

	for(int i = 0; i < N; i++) {
		string s;
		cnt[i].clear();

		cin >> s;

		if(i == 0) {
			model = process(s, cnt[i]);
		} else {
			string s1 = process(s, cnt[i]);
			
			if(s1 != model) {
				nice = false;
			}
		}
	}

	if(!nice) {
		cout << "Fegla Won\n";
	} else {
		cout << compute_ans(N) << "\n";
	}
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		test();
	}
}