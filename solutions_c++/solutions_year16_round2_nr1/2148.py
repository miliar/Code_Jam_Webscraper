#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
typedef pair<int, int> pii;

string desc[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<int> cnt(27);
vector<int> ans;

bool go(int f) {
	bool can = true;
	for(int i=0;i<desc[f].size();i++) {
		int pos = desc[f][i]-'A';
		cnt[pos]--;
		if (cnt[pos] < 0)
			can = false;
	}
	if (can) {
		ans.push_back(f);
		bool over = true;
		for (int i=0;i<26;i++) if (cnt[i] > 0) {
			over = false;
			break;
		}
		if (over || go(f))
			return true;
		ans.pop_back();
	}
	for(int i=0;i<desc[f].size();i++) {
		cnt[desc[f][i]-'A']++;
	}

	if (f == 0 && cnt['Z'-'A'] > 0)
		return false;
	if (f == 2 && cnt['W'-'A'] > 0)
		return false;
	if (f == 4 && cnt['U'-'A'] > 0)
		return false;
	if (f == 6 && cnt['X'-'A'] > 0)
		return false;
	if (f+1 <= 9)
		return go(f+1);
	else
		return false;
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		printf("Case #%d: ", t);
		string s;
		cin>>s;
		ans.clear();
		for(int i=0;i<27;i++) cnt[i]=0;
		for(int i=0;i<s.size();i++) cnt[s[i]-'A']++;
		go(0);
		for(int i=0;i<ans.size();i++) cout << ans[i];
		cout << endl;
	}
	return 0;
}
