#include <bits/stdc++.h>
using namespace std;

#define FOR(i, to, from) for(int i=to; i<from; i++)
#define ri(n) scanf("%d", &n)
#define rii(n, m) scanf("%d %d", &n, &m);
#define ms(obj,val) memset(obj, val, sizeof(obj))
#define pb push_back
typedef long long ll;
typedef vector<int> vi;

string S;
int n;
vi P, F;
int T;
int main(){
	cin >>T;
	FOR(t, 1, T+1){
		cout <<"Case #"<< t << ": ";
		P.clear(); F.clear();
		cin >> S;
		n = S.length();
		int M = S[0];
		P.pb(0);
		FOR(i, 1, n){
			if(S[i]>=M){
				M = S[i];
				P.pb(i);
			}
			else F.pb(i);
		}
		int k1 = P.size(), k2 = F.size();
		for(int i=k1-1; i>=0; i--) cout << S[P[i]];
		FOR(i, 0, k2) cout << S[F[i]];
		cout << endl;
	}	
}
