#include <bits/stdc++.h>
using namespace std;

inline char change(char c) {
	return c == '+' ? '-' : '+';
}

void my_reverse(string &s, int &cot, int st, int ed)
{
	int ptr_front = st, ptr_back = ed - 1;
	while (ptr_front <= ptr_back) {
		swap(s[ptr_front], s[ptr_back]);
		++ptr_front, --ptr_back;
	}
	for (int i = st; i < ed; ++i) {
		s[i] = change(s[i]);
	}
	++cot;
}

int main()
{
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	freopen("out_large.txt", "w", stdout);
#endif
	int t, cas = 0;
	string s;
	cin >> t;
	while (t-- && cin >> s) {
		int cot = 0, ptr_back = s.length() - 1;
		bool flag = 1;
		while (flag) {
			flag = 0;
			for (int i = ptr_back; i >= 0; --i) {
				if (s[i] == '-') {
					bool plus_flag = 0;
					for (int j = 0; j <= i; ++j) {
						if (s[j] == '+') {
							plus_flag = 1;
						}
						if (s[j] == '-'){
							if (plus_flag) {
								my_reverse(s, cot, 0, j);
							}
							break;
						}
					}
					my_reverse(s, cot, 0, i + 1);
					ptr_back = i - 1;
					flag = 1;
					break;
				}
			}
		}
		cout << "Case #" << ++cas << ": " << cot << endl;
	}
	return 0;
}
