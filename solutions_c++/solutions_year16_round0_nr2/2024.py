#include <iostream>
#include <string>
#include <set>
#include <queue>

using namespace std;

int getAnsFast(string str) {
	if (str.length() == 1) {
		return str[0] == '+' ? 0 : 1;
	}
	int count = 0;
	char curr = str[0];
	for (int i = 0; i < str.length(); i++) {
		if (str[i] != curr) {
			count++;
			curr = str[i];
		}
	}
	if (curr != '+') count++;
	return count;
}

int getAns(string str) {
	queue<pair<string, int> > q;
	set<string> seen;

	q.push(pair<string, int>(str, 0));
	while(!q.empty()) {
		pair<string, int> curr = q.front();
		q.pop();

		string str = curr.first;
		int steps = curr.second;
		bool done = true;
		for (int i = 0; i < str.length(); i++) {
			if (str[i] != '+') {
				done = false;
				break;
			}
		}
		if (done) return steps;

		for (int i = 1; i <= str.length(); i++) {
			string str2 = str;
			for (int j = 0; j < i/2; j++) {
				char tmp = str2[j];
				str2[j] = str2[i-1-j];
				str2[i-1-j] = tmp;
			}
			for (int j = 0; j < i; j++) {
				str2[j] = ((str2[j] == '+') ? '-' : '+');
			}
			if (seen.count(str2) == 0) {
				seen.insert(str2);
				q.push(pair<string, int>(str2, steps+1));
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int nt; cin >> nt;
	for (int ct = 1; ct <= nt; ct++) {
		string str; cin >> str;
		//int ans = getAns(str);
		int ans = getAnsFast(str);
		cout << "Case #" << ct << ": " << ans << endl;
	}
}
