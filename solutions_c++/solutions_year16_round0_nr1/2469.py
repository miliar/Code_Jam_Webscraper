#include <bits/stdc++.h> 
#define X first
#define Y second
#define mp make_pair
#define pb push_back

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef pair<ll, ll> pll;

template<class T> inline T maxm(T& a, T b){return a = a < b ? b : a;}
template<class T> inline T minm(T& a, T b){return a = a > b ? b : a;}

bool vis[10];

void visitDigits(ll n){
    while(n){vis[n%10] = 1; n /= 10;}
}

bool allDone(){

    for(int d = 0; d < 10; ++d) if(!vis[d]) return 0;
    return 1;
}

int main(){

    int T;
    cin >> T;


    for(int i = 0; i < T; i++){
    
	memset(vis, 0, sizeof(vis));
	ll n;
	cin >> n;

	if(!n) cout << "Case #" << i + 1 << ": INSOMNIA\n";
	else{

	    int j;
	    for(j = 1;;++j) {
		visitDigits(n * j);
		assert(n * j > 0);
		if(allDone()){
		    cout << "Case #" << i + 1 << ": " << n * j << '\n';
		    break;
		}
	    }
	}
    
    }

    return 0;

}
