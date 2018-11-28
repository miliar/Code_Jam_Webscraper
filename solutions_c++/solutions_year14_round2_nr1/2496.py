#include <cstdio>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

int array[101][101];
string a;
string b;
int n;

void read() {
	cin >> n;
	cin >> a >> b;
	a = " " + a + " ";
	b = " " + b + " ";
}

void solve() {
	int i = 1, j = 1;
	int x = 0;
	bool first_try = true;
	while (i != a.length() && j != b.length()) {
		if (a[i] == b[j]) {
			i++;
			j++;
			first_try = true;
		} else if (a[i] == a[i-1]) {
			i++;
			x++;
			first_try = true;
		} else if (first_try) {
			int temp = i;
			i = j;
			j = temp;
			string stemp = a;
			a = b;
			b = stemp;
			first_try = false;
		} else {
			cout << "Fegla Won" << endl;
			return;
		}
	}
	cout << x << endl;
}

int main() {
    freopen("inputA.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	
    int cases;
    cin >> cases;
    for (int count = 1; count <= cases; count++) {
		read();
        cout << "Case #" << count << ": ";
		solve();
    }
    return 0;
}