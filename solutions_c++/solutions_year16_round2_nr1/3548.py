#include <bits/stdc++.h>
using namespace std;
#define clc(x) memset(x, 0, sizeof(x))
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define F0(i, n) for (int i = 0; i < n; i++)
#define F1(i, n) for (int i = 1; i <= n; i++)
typedef long long ll;
const ll mxn = 1e4 + 5;
int T;
int ans;
string accd[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string number[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
int a[10];
string ts(int i, int j) {
	string s;
	while (j--) {
		s += accd[i];
	}
	return s;
}

int main() {
    freopen("/Users/akanork/Desktop/1.in", "r", stdin);
    freopen("/Users/akanork/Desktop/1.out", "w", stdout);
    scanf("%d", &T);
    int kase = 1;
    while (T--) {
    	int a57 = 0, a38 = 0;
    	clc(a);
    	ans = 0;
    	string s;
    	cin >> s;
    	string s1 = s;
    	sort(s1.begin(), s1.end());
    	F0(i, s.length()) {
    		if (s[i] == 'Z') a[0]++;
    		if (s[i] == 'W') a[2]++;
    		if (s[i] == 'U') a[4]++;
    		if (s[i] == 'X') a[6]++;
    		if (s[i] == 'V') a57++;
    		if (s[i] == 'H') a38++;
    	}
    	int len = s.length() / 3;
    	bool flag = false;
    	F0(x1, len+2){
    		F0(x3, a38+2) {
    			F0(x5, a57+2) {
    				F0(x7, a57+2) {
    					F0(x8, a38+2){
    						F0(x9, len+2) {
    							string tmp = ts(0, a[0]) + ts(1, x1) + ts(2, a[2]) + ts(3, x3) + ts(4, a[4]) + ts(5, x5)
    							+ ts(6, a[6]) + ts(7, x7) + ts(8, x8) + ts(9, x9);
    							sort(tmp.begin(), tmp.end());
    							if (s1 == tmp) {flag = true; a[1] = x1; a[3] = x3; a[5] = x5; a[7] = x7; a[8] = x8; a[9] = x9; break;}
    						}
    						if(flag) break;
    					}
    					if(flag) break;
    				}
    				if(flag) break;
    			}
    			if(flag) break;
    		}
    		if(flag) break;
    	}

    	string ans2;
    	F0(i, 10) {
    		// printf("a[%d] = %d\n", i, a[i]);
    		while (a[i]--)
    			ans2 += number[i];
    	}

    	cout << "Case #" << kase++ << ": " << ans2 << endl;

    	
   }
	return 0;
}