#include<iostream>
#include<string>
using namespace std;

int main() {
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int t, it, smax, i, friends, total, current;
	string line;
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> smax >> line;
		total = friends = 0;
		for (i = 0; i < line.size(); i++) {
			current = line[i] - '0';
			if (total < i) {
				friends += i - total;
				total = i;
			}
			total += current;
		}
		cout << "Case #" << it << ": " << friends << '\n';
	}
	return 0;
}