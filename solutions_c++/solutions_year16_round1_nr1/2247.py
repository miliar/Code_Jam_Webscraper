#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
int main() {
	FILE *fin = freopen("A-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		string n;
		cin >> n;
		string result = "";
		char first = n.at(0);
		for (int i = 0; i < n.length(); i++) {
			if (n.at(i) < first) {
				result = result + n.at(i);
			}
			else {
				first = n.at(i);
				result = n.at(i) + result;
			}
		}
		cout << result << endl;
	}
	exit(0);
}
