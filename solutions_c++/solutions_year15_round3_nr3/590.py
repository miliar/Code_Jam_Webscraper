#include <iostream>

using namespace std;


int main() {
 	int T;
 	cin >> T;
 	for (int I = 1; I<=T; I++) {
 	 	int m, d, v;
 	 	int c[5];
 	 	bool p[100]={0};
 	 	cin >> m >> d >> v;
 	 	for (int i = 0; i < d; i++) {
 	 		cin >> c[i];
 	 	}
 	 	p[0] = 1;
 	 	for (int i = 0; i < d; i++) {
 	 	 	for (int j = v; j >= c[i]; j--) {
            	p[j] |= p[j-c[i]];
            }
 	 	}
 	 	int ans = 0;
 	 	for (int k = 1; k <= v; k++) {
 	 	 	if (!p[k]) {
 	 	 	    ans++;
 	 	 	    for (int j = v; j >= k; j--) {
 	 	 	     	p[j] |= p[j-k];
 	 	 	    }
 	 	 	}	
 	 	}
 		cout << "Case #"<<I<<": " << ans << '\n';
 	}
}