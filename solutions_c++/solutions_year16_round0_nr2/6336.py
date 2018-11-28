#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
		string pieStack;
		cin >> pieStack;
		int flipTime = 0;
		char tracking = '+';
		int n = pieStack.length();
		for (int i = n-1; i >= 0; i--) {
		    char onePie = pieStack[i];
            if (onePie != tracking) {
                flipTime += 1;
                tracking = onePie;
            }
		}

		cout << "Case #" << t << ": ";
		cout << flipTime << endl;
	}
	exit(0);
}
