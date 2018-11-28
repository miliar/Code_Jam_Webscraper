#include <iostream>
#include <string>

using namespace std;

int k, l, n;
string s, t;
typedef long double ldouble;

ldouble f (string x) {	
	ldouble ans = 0;
	if ((int)x.size()==n) {
	    for(int i = 0; i < n; i++) {
	     	int j = i;
	     	while (j < n && x[j]==t[j-i]) j++;
	     	if (j-i == (int)t.size()) {
	     	 	ans += 1;
	     	}
	    }                                  
	    for (int i = 0; i < n; i++) ans/=k;
	} else {
		for (int i = 0; i < k; i++) {
		 	ans += f(x+s[i]);
		}
	}
	return ans;	
}

int main() {
 	int T;
 	cin >> T;
 	for (int I = 1; I<=T; I++) {
 	 	cin>> k >> l >> n;
		cin >> s >> t;

		bool ok = 1;
		for(int i = 0; i < l; i++) {
			ok = 0;
			for (int j = 0; j < k; j++)
				if(t[i]==s[j]) ok = 1;
			if(!ok) break;
		}

		ldouble ans;

		if(!ok) {
        	ans = 0;
        } else {
        	int st = l;
        	for (int i = 1; i < l; i++) {
        		int j = i;
        		while (j < l && t[j]==t[j-i]) j++;
        		if(j==l) {
                	st = i;
                	break;
                }
        	}	
        	ans = (n-l)/st + 1;
        	ans -= f("");
        }
        cerr << I << "\n";
        cout.precision(8);
 		cout << "Case #"<<I<<": " << ans << '\n';
 	}
}