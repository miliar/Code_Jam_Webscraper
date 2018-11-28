#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("a.out","wt",stdout);
	int T;
	cin >> T;
	for (int I = 1; I <= T; I++) {    	
		int n, m[2000];
		cin >> n;
		for(int i = 0; i < n; i++) cin >> m[i];
		int y = 0;
		int v = 0;
		int z = 0;
		for(int i = 1; i < n; i++) {
			if (m[i] < m[i-1]) {
				y += m[i-1] - m[i];
		    	v = max(v, m[i-1] - m[i]);
		    }
		}
		for(int i = 0; i < n-1; i++) {
		   	z += min(m[i], v);
		}	
		cout << "Case #" << I << ": " << y << " " << z << "\n";
	}
	return 0;
}