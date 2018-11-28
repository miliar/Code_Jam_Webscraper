#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cs;
	cin >> cs;
	for (int cc = 1; cc <= cs; cc++) {
		int n;
		string s;
		cin >> n >> s;
		n++;
		for (int i = 0; i < s.size(); i++)
			s[i] -= '0';
		vector<int> p(n);
		for (int i = 1; i < n; i++)
			p[i] = s[i - 1] + p[i - 1];
		int t = 0;
		for (int i = 1; i < n; i++) {
			t += max(0, i - p[i] - t);
			//cout << t << "\n";
		}
		cout << "Case #" << cc << ": " << t << "\n";
	}
}
