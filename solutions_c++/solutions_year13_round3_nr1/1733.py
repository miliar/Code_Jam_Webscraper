#include<iostream> 
#include<cstdio> 
#include<cmath> 
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<cassert>
#include<queue>

#define LL long long
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>
#define pb push_back

using namespace std;



int main() {
	#ifdef DEBUG
	freopen("a.in", "r", stdin);
	freopen(".out", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
    	int prev = 0, n, ans = 0;
    	string s;
    	cin >> s >> n;
    	for (int i = 0; i < s.size(); i++) {
    		if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u') {
    			int cnt = 1, last = i;
    			if (cnt != n)
    				for (int j = i + 1; j < s.size(); j++)
			    		if (s[j] != 'a' && s[j] != 'e' && s[j] != 'i' && s[j] != 'o' && s[j] != 'u') {
			    			cnt++;
			    			if (cnt == n) {
			    				last = j;
			    				break;
			    			}
			    		}
			    		else
			    			break;
    			if (cnt == n) {
    				ans += (s.size() - last) * (i - prev + 1);
    				cerr << ans << ' ';
    				prev = i + 1;
    			}
    		}
    	}

    	cerr << endl;
    	cout << "Case #" << test + 1 << ": " << ans << endl;
    }

	return 0;
}