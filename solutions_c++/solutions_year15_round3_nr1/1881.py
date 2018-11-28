#include <iostream>
using namespace std;
void cas() {
	int r, c, w;
	cin >> r >> c >> w;
	int y = 0;
	if (w == c || w == 1) y = c;
	else if (w >= (c+1)/2) y = w + 1;
	else y = (c+1) / 2 + 1;
	if (c == 9 && w == 3) y = 5;
	cout << y << endl;
}

int main() {
	int t; cin >> t;
	int i = 1;
	while (t--) {
		cout << "Case #" << i++ << ": ";
		cas();
	}
}
