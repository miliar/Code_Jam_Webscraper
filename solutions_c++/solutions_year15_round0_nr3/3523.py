#include <string>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

string table[4][4] = {"1","i","j","k",
					  "i","-1","k","-j",
					  "j","-k","-1","i",
					  "k","j","-i","-1"};

map<char,int> m;

bool check(string s) {

	vector<int> vi;
	vector<int> vk;
	char now;
	bool neg;

	neg = false;
	now = '1';
	for (int i = 0; i < s.length()-2; i++) {
		string mul = table[m[now]][m[s[i]]];
		now = mul[mul.length()-1];
		if (mul[0] == '-')
			neg = !neg;

		if (!neg && now == 'i') {
			vi.push_back(i);
		}
	}

	neg = false;
	now = '1';
	for (int i = s.length()-1; i > 1; i--) {
		string mul = table[m[s[i]]][m[now]];
		now = mul[mul.length()-1];
		if (mul[0] == '-')
			neg = !neg;

		if (!neg && now == 'k') {
			vk.push_back(i);
		}
	}

	reverse(vk.begin(),vk.end());

	if (vi.size() == 0 || vk.size() == 0)
		return false;

	int start, end = vk[vk.size()-1];

	for (int i = 0; i < vi.size(); i++) {
		start = vi[i]+1;
		neg = false;
		now = '1';
		for (int j = start; j < end; j++) {
			string mul = table[m[now]][m[s[j]]];
			now = mul[mul.length()-1];
			if (mul[0] == '-')
				neg = !neg;

			if (!neg && now == 'j' && binary_search(vk.begin(),vk.end(),j+1)) {
				return true;
			}
		}
	}

	return false;
}

int main() {

	m['1'] = 0;
	m['i'] = 1;
	m['j'] = 2;
	m['k'] = 3;

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int L,X;
		cin >> L >> X;
		string s;
		cin >> s;
		string input = "";
		for (int i = 0; i < X; i++) {
			input = input + s;
		}

		if (check(input))
			printf("Case #%d: YES\n",tc);
		else
			printf("Case #%d: NO\n",tc);

	}
	return 0;
}