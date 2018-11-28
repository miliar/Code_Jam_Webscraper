#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string gpattern(string raw) {
	int pi = 0;
	string pattern;
	for (int i=0;i<raw.length();i++) {
		if (pattern.empty() || pattern[pi-1] != raw[i]) {
			pattern.push_back(raw[i]);
			pi++;
		}
	}
	return pattern;
}

vector<int> csets(string raw) {
	vector<int> cs;
	int pi = 0;

	for (int j=0;j<raw.length();j++,pi++) {
		int count = 1;
		while (j+1<raw.length() && raw[j+1]==raw[j]) {
			j++;
			count++;
		}
		cs.push_back(count);
	}
	return cs;
}

int main() {
  int T, N;
  cin >> T;
  for (int t=1;t<=T;t++) {
		cin >> N;
		string pattern;
		string raw;
		vector<int> mn,mx;
		cin >> raw;
		int pi = 0;
		pattern = gpattern(raw);
		mn = csets(raw);
		mx = mn;
		bool matches = true;
		for (int i=1;i<N;i++) {
			pi = 0;
			cin >> raw;
			if (pattern != gpattern(raw)) matches = false;
			if (!matches) continue;
			vector<int> counts = csets(raw);

			for (int j=0;j<pattern.length();j++) {
				mn[j] = min(mn[j],counts[j]);
				mx[j] = max(mx[j],counts[j]);
			}
		}
		printf("Case #%d: ", t);
		if (!matches) cout << "Fegla Won" << endl;
		else {
			int count = 0;
			for (int i=0;i<pattern.length();i++) {
				count += mx[i]-mn[i];
			}
			printf("%d\n",count);
		}
	}

  return 0;
}
