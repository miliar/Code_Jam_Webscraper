#include <iostream>
#include <cstdio>
#include <cmath>
#define min(a,b) (a<b ? a : b)

using namespace std;

int main() {
	freopen("c.out","wt",stdout);
	int T;
	cin >> T;
	for (int I = 1; I <= T; I++) {    	
		int n;
	    cin >> n;
	    long long x[20], y[20], ans[20]={0};
	    for (int i = 0; i < n; i++) {
	      	cin >> x[i] >> y[i];
	    } 
	    for (int i = 0; i < n; i++) {
	    	ans[i] = 1000;
	    	for (int j = 0; j < n; j++) {
	    		int t = 0;
         		for (int h = 0; h < n; h++) {
         			long long s = x[i]*y[j]-x[j]*y[i] + x[j]*y[h]-x[h]*y[j] + x[h]*y[i]-x[i]*y[h];
         		 	if(s > 0) t++; 	
         		// 	if(i==4) cerr << i << j << h << " " << s <<'\n';
         		}
         		if (i!=j) ans[i] = min(ans[i], t);
         	}
	    }
	    if(n==1) ans[0]=0;
		cout << "Case #" << I << ":\n";
		for(int i = 0; i < n; i++) cout << ans[i] << '\n';
	}
	return 0;
}