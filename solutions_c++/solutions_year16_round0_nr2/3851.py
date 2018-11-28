#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) int((c).size())
#define REP(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;
const int MAX = 1100100;

int T, N, sol;
string s;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> T;
	REP(tc, T){
		cin >> s;
		sol = 0;
		REP(I, SZ(s)-1) sol += s[I]!=s[I+1];
		cout << "Case #" << tc+1 << ": " << (sol+ (s.back()=='-')) << '\n';
	}
}
