#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve(int ind) {
    // input
    int Smax;
    string S;
    cin >> Smax >> S;

    // process
    int nUp = 0;
    int add = 0;
    int d;
    for (int nextUp = 0; nextUp <= Smax; ++nextUp) {
	d = 0;
	if (nUp < nextUp) {
	    d = nextUp - nUp;
	}
	nUp += (S[nextUp] - '0') + d;
	add += d;
    }
    
    // output
    cout << "Case #" << ind << ": " << add << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}