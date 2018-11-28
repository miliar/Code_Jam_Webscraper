#include <iostream>
#include <cstdio>

using namespace std;

int lcm(int a, int b){
 	for(int i=a;;i+=a) {
 		if (!(i%b)) return i;
 	}
}

int main() {
	freopen("b.out","wt",stdout);
	int T;
	cin >> T;
	for (int I = 1; I <= T; I++) {    	
	    int b, n;
	    int m[2000];
	    cin >> b >> n;
	    for (int i = 0; i < b; i++) cin >> m[i]; 
	    int l = m[0];
	    for (int i = 1; i < b; i++) l = lcm(l, m[i]);
	    int k = 0;
	    for(int i = 0; i < b; i++) k += l/m[i];
	    n %= k;
	    if (!n) n = k;
//	    cerr << n << '\n';
	    int bb = 1;
	    int wt[6]={0};
	    while (n) {
	    	int minw = 1000;
       	 	for (int j = 0; j < b; j++) {
       	 	 	if(wt[j]==0) {
       	 	 		bb = j+1;
       	 	 	    wt[j] = m[j];
       	 	 	    n--;
       	 	 	    if(!n) break;
       	 	 	}	
       	 	 	minw = min(minw, wt[j]);
       	 	}
       	 	for (int j = 0; j < b; j++) wt[j] -= minw;
       	}
		cout << "Case #" << I << ": " << bb << '\n';
	}
	return 0;
}