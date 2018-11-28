#include "bits/stdc++.h"
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; cin >> kase;
	for (int i = 0; i < kase; ++i)
	{
		string s;
		cin >> s;
		string t;
		int size = s.size();
		t.append(1,s[0]);
		for (int k = 1; k < size; ++k)
		{
			if (s[k] >= t[0])
				t.insert(t.begin(),s[k]);
			else
				t.append(1,s[k]);
		}
		cout << "Case #" << i + 1 << ": " << t << endl;
	}
	return 0;
}
