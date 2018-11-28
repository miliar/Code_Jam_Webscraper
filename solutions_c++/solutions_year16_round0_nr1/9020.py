#include<iostream>
#include<set>

using namespace std;

void solve(int n) {
	set<int> d;
	if (n == 0) {
		cout << "INSOMNIA";
		return;
	}
	long long c = n;
	do {
		long long t = c;
		while (t) {
			d.insert(t % 10);
			t /= 10;
		}
		c += n;
	} while (d.size() != 10);
	cout << c - n;
}


int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    int n;
    cin >> n;
    solve(n);
    cout << endl;
  }
  return 0;
}
