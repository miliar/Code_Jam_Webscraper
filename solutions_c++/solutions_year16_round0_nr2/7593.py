#include <bits/stdc++.h>
#define f first
#define s second
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)

using namespace std;

double eps = 1e-9;
const int INF = 1e9+7;
const int MAXN = int (3e5+7);

int T, n;

int main () { 
   	//freopen("input.in", "r", stdin);
   	//freopen("output.txt", "w", stdout);  
    
    cin >> T;
    for(int w = 0; w < T; w ++) {
    	int ans = 0;
    	string s;
    	cin >> s;
    	n = s.size();
    	char c = '+';
    	for(int i = n - 1; i >= 0; i --) {
    		if(s[i] != c) {
    			c = s[i];
    			ans ++;
    		}
    	}
    	cout << "Case " << "#" << w + 1 << ": " << ans << "\n";
    }
    return 0;
} 