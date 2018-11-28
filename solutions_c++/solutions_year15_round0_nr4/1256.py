#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main(){
 	int T;
 	cin >> T;
 	freopen("d.out","wt",stdout);
 	for (int I = 0; I < T; I++) {
 	    int x, r, c;
 	    cin >> x >> r >> c;
 	    bool win = 0;
 	    if (r*c % x) win = 1;
 	    else {
 	    	if (x<3) win = 0;
 	    	else if (x == 3) {
 	    		win = (r==1 || c==1);
 	    	} else {
 	    	    win = (r+c < 7);
 	    	}
 	    }
 		cout << "Case #" << I+1 << ": ";
 		cout << (win?"RICHARD":"GABRIEL") << '\n';
 	}                                    
 	return 0;
}