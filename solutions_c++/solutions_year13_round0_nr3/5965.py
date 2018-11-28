# include <iostream>
# include <vector>
# include <fstream>
# include <sstream>
# include <string>
# include <cmath>
# include <algorithm>

using namespace std;

int check(int n) {
    stringstream xz;
    string numstr;
    xz << n;
    xz >> numstr;
    string numrev;
    numrev = numstr;
    reverse(numrev.begin(), numrev.end());
    stringstream yy;
    int revnum;
    yy << numrev;
    yy >> revnum;
    if (revnum == n) return 1;
    return 0;
}

int PAL[1050];
int FSQ[1050];
int CUM[1050];
int is_palindrome(int num) {
    if (PAL[num] == -1) return 0;
    else if (PAL[num] == 1) return 1;
    else return check(num);
}

void compute_primes() {
    for (int i = 0; i <= int(sqrt(1000))+1; i++) {
	if (i*i <= 1000) {
	    if (is_palindrome(i)) {
		if (is_palindrome(i*i)) {
		    FSQ[i*i] = 1;
		}
	    }
	}
    }
}

void cumulate() {
    CUM[0] = FSQ[0];
    for (int i = 1; i <= 1000; i++) {
	CUM[i] = FSQ[i] + CUM[i-1];
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    int Ti=0;
    compute_primes();
    cumulate();
    while (Ti++ < T) {
	int A, B;
	cin >> A >> B;
	printf("Case #%d: %d\n", Ti, CUM[B] - CUM[A-1]);
    }
    return 0;
}
