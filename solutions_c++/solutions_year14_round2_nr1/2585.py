#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>	
#include <vector>

#define maxxN 102

using namespace std;

int T, N;
int maxx[maxxN];
int minn[maxxN];
vector< pair<char, int> > data [maxxN];

void getData(int cnt, int pos2) {
	if(maxx[pos2] < cnt) {
		maxx[pos2] = cnt;
	}

	if(minn[pos2] > cnt) {
		minn[pos2] = cnt;
	}

}

void proc(int pos, string str) {
	char ch = str[0];
	int cnt = 1;

	for (int i=1; i < str.size(); i++) {
		if(str[i] == str[i-1]) {
			cnt++;
		} else {
			data[pos].push_back(make_pair(ch, cnt));
			getData(cnt, data[pos].size()-1);
			ch = str[i];
			cnt = 1;
		}
	}

	data[pos].push_back(make_pair(ch, cnt));
	getData(cnt, data[pos].size()-1);
}

int solve() {
	for (int i=1; i < N; i++) {
		if (data[i].size() != data[i-1].size()) {
			return -1;
		}
		for(int j=0; j < data[i].size(); j++) {
			if(data[i][j].first != data[i-1][j].first) {
				return -1;
			}
		}
	}

	int ares = 0;
	for (int i=0; i < data[0].size(); i++) {
		int res = 1000;
		for(int j=minn[i]; j <= maxx[i]; j++) {
			int val = 0;
			for (int k=0; k < N; k++) {
				if(data[k][i].second < j) {
					val += j - data[k][i].second;
				} else {
					val += data[k][i].second - j;
				}
			}
			if (val < res) {
				res = val;
			}
		}
		ares += res;
		
	}

	return ares;
}

int main() {
	string str;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		for (int i=0; i < N; i++) {
			data[i].clear();
			for(int i=0; i < maxxN; i++) {
				maxx[i] = 0;
				minn[i] = 1000;
			}
		}
		for(int i=0; i < N; i++) {
			cin >> str;
			proc(i, str);
		}
		cout << "Case #" << t << ": ";
		int res = solve();
		if(res == -1) {
			cout << "Fegla Won" << endl;
		} else {
			cout << res << endl;
		}
	}
	return 0;
}