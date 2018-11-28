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

string s;
void flip(int i){
    for(int j = 0; j < i; j++) s[j] = (s[j] == '+' ? '-' : '+'); 
}

int main(){

    int T;
    cin >> T;

    //s = "-------";
    for(int i = 0; i < T; ++i){
    
	cin >> s;
	int cnt = 0;
	int N = s.size();
	//cerr << s << '\n';
	for(int i = N - 1; i >= 0; --i){
	    if(s[i] == '-') {
		flip(i + 1);
		++cnt;
	    }
	    //cerr << s << '\n';
	}

	cout << "Case #" << i + 1 << ": " << cnt << '\n';
    
    }

    return 0;

}
