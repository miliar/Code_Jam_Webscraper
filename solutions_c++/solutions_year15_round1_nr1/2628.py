#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cs;
	cin >> cs;
	for (int cc = 1; cc <= cs; cc++) {
		int n;
		cin >> n;
		vector<int> d(n);
		for (int i = 0; i < n; i++)
			cin >> d[i];
		int a = 0;
		for (int i = 0; i < n - 1; i++)
			if (d[i] > d[i + 1])
				a += d[i] - d[i + 1];
		int b = 0, c = 0;
		for (int i = 0; i < n - 1; i++)
			if (d[i] - d[i + 1] > c)
				c = d[i] - d[i + 1];
		for (int i = 0; i < n - 1; i++)
			if (d[i] > c)
				b += c;
			else b += d[i];
		cout << "Case #" << cc << ": " << a << " " << b << "\n";
	}
}
