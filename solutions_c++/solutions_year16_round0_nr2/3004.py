#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;

int main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		string str;
		cin >> str;
		int num = str.length();
		bool happy[num];
		int j = num-1;
		for (int i = 0; i < num; i++) {
			if (str[j] == '+') {
				happy[i] = 1;
			}
			else {
				happy[i] = 0;
			}
			j--;
		}
		int flips = 0;
		int trav = 0;
		while (trav < num) {
			if (happy[trav]) {
				trav++;
			}
			else {
				flips++;
				int top = num-1;
				if (happy[top]) {
					flips++;
				}
				while (happy[top]) {
					happy[top] = 0;
					top--;
				}
				int numcake = num - trav;
				if (numcake%2) {
					happy[trav+numcake/2] = !happy[trav+numcake/2];
				}
				for (int i = 0; i < numcake/2; i++) {
					if (happy[trav+i] == happy[num-i-1]) {
						happy[trav+i] = !happy[trav+i];
						happy[num-i-1] = !happy[num-i-1];
					}
				}
			}
		}
		cout << flips << endl;
	}
	exit(0);
}