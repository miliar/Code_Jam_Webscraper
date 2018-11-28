#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;

int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'
    int T; cin >> T;
    for(int tt = 1; tt <= T; tt++){
    	cout << "Case #" << tt << ": ";
    	string pan;
    	int k; cin >> pan>> k;
    	int ans = 0;
    	for(int i = 0; i < (int)pan.size() - k + 1; i++){
    		if(pan[i] == '-'){
    			for(int j = i; j < i + k; j++){
    				if(pan[j] == '-')pan[j] = '+';
    				else pan[j] = '-';
    			}
    			ans++;
    		}

    	}
    	for(int i = (int)pan.size() - k + 1; i < (int)pan.size(); i++){
    		if(pan[i] == '-'){
    			ans = -1; break;
    		}
    	}
    	if(ans == -1)cout << "IMPOSSIBLE" << endl;
    	else cout << ans << endl;

    }


}

