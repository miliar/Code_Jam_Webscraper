#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) int((c).size())
#define REP(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;

int T, N;

int solve(int N){
	set<int> S;
	for(int n=N; true; n+=N){
		int m = n;
		while(m > 0){
			S.insert(m%10);
			m /= 10;
		}
		if (SZ(S)==10) return n;
	}
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> T;
	REP(tc, T){
		cin >> N;
		
		cout << "Case #" << tc+1 << ": ";
		if (N==0) cout << "INSOMNIA" << endl;
		else      cout << solve(N) << endl;
	}
}
