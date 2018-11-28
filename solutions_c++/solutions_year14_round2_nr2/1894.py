#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
	int A, B, K;
	cin >> A >> B >> K;

	int res = 0;
	for (int a = 0; a < A; a++) {
	    for (int b = 0; b < B; b++) {
		if ((a & b) < K) {
		    res++;
		}
	    }
	}
	cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
