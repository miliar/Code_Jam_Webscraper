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

ll p81(ll n){
    return n * n * n * n * n * n * n * n + 1;
}
ll p161(ll n){
    return (p81(n) - 1) * (p81(n) - 1) + 1;
}

int main(){

    int T;
    cin >> T; 
    assert(T == 1);

    for(int i = 0; i < T; ++i){
	int N;
	int J;
	cin >> N >> J;
    //assuming that N is even
	//assert(N == 16 && J == 50);

	vector<ll> bigList;
	int cnt = 0;
	cout << "Case #" << i + 1 << ":\n";
	for(ll j = 1; j < min(1<<14, J + 1); ++j){
	    ll midNum;
	    midNum = 2 * j + 2 * (1<<14) + 1;
	    //bigList.pb(midNum + midNum<<(N / 2));
	    bitset<16> b(midNum);
	   
	    cout << b << b << ' ' << p161(2) << ' ' << p161(3) << ' ' << 
		p161(4) << ' ' << p161(5) << ' ' << p161(6) << ' ' <<  
		p161(7) << ' ' << p161(8) << ' ' << p161(9) << ' ' << p161(10) << '\n';
	}


    }
    return 0;

}
