#include <bits/stdc++.h>

using namespace std;

int find_last_blank(const vector<bool>& pancakes, int hint) {
	for (int i = hint-1; i >= 0; --i) {
		if (!pancakes[i]) return i;
	}
	return -1;
}

vector<bool> parse_str(string pancake_str) {
	vector<bool> res(pancake_str.size());
	for (size_t i = 0; i < res.size(); ++i)
		res[i] = (pancake_str[i] == '+');
	return res;
}

void print_vec(vector<bool>& v) {
	for (size_t i = 0; i < v.size(); ++i)
		cout << v[i] << " ";
	cout << endl;
}

void flip(std::vector<bool>& pancakes, int k) {
	for (int i = 0; i < k; ++i) {
		pancakes[i] = !pancakes[i];
	}
	reverse(pancakes.begin(), pancakes.begin()+k);
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		string pancake_str;
		cin >> pancake_str;
		vector<bool> pancakes = parse_str(pancake_str);
		int op_count = 0;
		int last_blank = find_last_blank(pancakes, pancakes.size());
		while (last_blank != -1) {
			int k = -1;
			while (pancakes[++k]);
			if (k > 0) {
				flip(pancakes, k);
				++op_count;
			}
			flip(pancakes, last_blank+1);
			++op_count;
			last_blank = find_last_blank(pancakes, last_blank);
		}
		cout << op_count << endl;
	}
	return 0;
}