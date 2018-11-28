#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

int t;
char c[111];
int n;
void solve(){
	scanf("%s", c);
	n = strlen(c);
	int ans = 0;
	while(true){
		int index = n-1;
		while(index >= 0 && c[index] == '+') index--;
		if(index < 0) break;
		ans++;
		for(int i =0;i<=index; i++){
			if(c[i] == '+') c[i] = '-';
			else c[i] = '+';
		}
	}
	printf("%d\n", ans);
}


int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif
    scanf("%d", &t);
    for(int i =0;i<t;i++){
    	printf("Case #%d: ", i+1);
    	solve();
    }




    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}


