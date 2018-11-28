#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main(){
 	int T;
 	cin >> T;
 	freopen("b.out","wt",stdout);
 	for (int I = 0; I < T; I++) {
 	    int d, p[3000], mint=0;
 	    cin >> d;
 	    for(int i = 0; i < d; i++) {
 	    	cin >> p[i];
 	    	mint = max(mint, p[i]);
 	    }
 	    for (int t = mint; t; t--) {
 	    	int dt = 0;
 	    	for(int i = 0; i < d; i++) {
 	    		dt += (p[i]+t-1)/t - 1;	 	
 	    	}
 	    	if (t+dt < mint) mint = t+dt;
 	    }
 		cout << "Case #" << I+1 << ": ";
 		cout << mint << '\n';
 	}
 	return 0;
}