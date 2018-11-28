#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

/*
5
4 11111
1 09
5 110011
0 1
4 30001
 */
#define TRACE(fmt,x) {fprintf(stderr,fmt,x);fprintf(stderr,"\n");}
#define CASE(a,b) fprintf(stderr, "%d / %d = %.2f | %.2f\n", a, b, (double)clock()/CLOCKS_PER_SEC, ((double)clock()/a*b)/CLOCKS_PER_SEC);

int m[1001];

int main() {
	int T;
	cin >> T;

	for (int t=1; t<=T; t++) {
		int N, i, j, k;
		cin >> N;

		string s;
		cin >> s;

		k = j = 0;
		for (i=0; i<=N; i++) {
			m[i] = s.at(i) - '0';
			if (m[i] > 0) {
				k += max(0, i - j);
				j += max(0, i - j);
			}
			j += m[i];
		}

		cout << "Case #" << t << ": " << k << endl;

		//CASE(t,T)
	}
	return 0;
}
