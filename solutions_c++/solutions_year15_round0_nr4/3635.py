#include <iostream>
#include <string>
 
using namespace std;
 
string solve() {
	int x, r, c;
	cin >> x >> r >> c;
	if (x == 1)
		return "GABRIEL";
	if (x == 2)
		if ((r * c) % 2 == 0 && r * c >= x)
			return "GABRIEL";
		else
			return "RICHARD";
	if (x == 3)
		if ((r * c) % 3 == 0 && r * c >= x)
			return "GABRIEL";
		else
			return "RICHARD";
	if (x == 4) {
		if ((r * c) % 4 != 0 || r * c < x)
			return "RICHARD";
		if (r > c)
			swap(r, c);
		if (r * c == 4)
			return "RICHARD";
		if (r == 2)
			return "RICHARD";
		return "GABRIEL";
	}
}
 
int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	return 0;
}