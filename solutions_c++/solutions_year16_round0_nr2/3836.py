#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define MAX_N 100
#define HAPPY '+'
#define BLANK '-'

using namespace std;

int R;
vector<char> v;

void input() {
	string temp;
	cin >> temp;
	v.resize(temp.length());
	for (int i = 0; i < temp.length(); i++) {
		v[i] = temp[i];
	}
}

bool check() {
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == BLANK) return false;
	}
	return true;
}

void flip(int n) {
	for (int i = 0; i <= n; i++) {
		v[i] = (v[i] == HAPPY) ? BLANK : HAPPY;
	}
	reverse(v.begin(), v.begin() + n + 1);
}

void process() {
	R = 0;
	while (!check()) {
		int i;
		for (i = 1; i < v.size(); i++) {
			if (v[i] != v[i - 1]) break;
		}
		flip(i-1);
		R++;
	}
}

void output(int t) {
	cout << "Case #" << t << ": " << R << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		input();
		process();
		output(i);
	}
	return 0;
}

