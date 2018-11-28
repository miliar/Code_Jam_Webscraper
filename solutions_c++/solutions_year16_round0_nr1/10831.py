#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    long long n;
    cin >> t;
    for (int i = 1; i <= t; i++) {
	cin >> n;
	if (n == 0) {
	    cout << "Case #" << i << ": INSOMNIA\n";
	    continue;
	}
	vector <bool> mark(10, false);
	int k = n, marked = 0;
	while (marked < 10) {
	    int temp = k;
	    while (temp > 0) {
		if (!mark[temp % 10]) {
		    marked++;
		    mark[temp % 10] = true;
		}
		temp /= 10;
	    }
	    k += n;
	}
	k -= n;
	cout << "Case #" << i << ": " << k << endl;
    }
    return 0;
}
