#include <cstdlib>
#include <stdio.h>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv){

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		int Smax, sm = 0;
		cin >> Smax;
		string s;
		cin >> s;
		int t = 0;
		for(int j = 0; j <= Smax; j++){
			int d = s[j]-'0';
			int m = max(0, j - t);
			sm += m;
			t += d + m;
		}
		cout << "Case #" << i << ": " << sm << endl;
	}
	return 0;
}