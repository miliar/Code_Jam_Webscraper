#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <ll> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ld> VD;
typedef vector <VD> VVD;
typedef vector <string> VS;
typedef vector <char> VC;
typedef vector <VC> VVC;
typedef pair <ll, ll> PII;
typedef pair <ll, PII> PIII;
typedef pair <ld, ld> PD;
typedef map <ll, ll> MII;
typedef map <string, int> MSI;
typedef queue <int> QI;
typedef queue <PII> QPI;
typedef set <ll> SI;
typedef SI::iterator IT;

#define F first
#define S second
#define pb push_back

struct Move{
	int p,r,s;
	string S;
};

int n,r,p,s;

Move compare (Move &A, Move &B){
	if (A.p == -1) return B;
	if (B.p == -1) return A;
	if (A.S < B.S) return A;
	return B;
}

int main(){
	
	vector <Move> P(14);
	vector <Move> S(14);
	vector <Move> R(14);
	
	Move m;
	m.p = 1;
	m.s = m.r = 0;
	m.S = "P";
	P[0] = m;
	
	m.s = 1;
	m.p = m.r = 0;
	m.S = "S";
	S[0] = m;
	
	m.r = 1;
	m.p = m.s = 0;
	m.S = "R";
	R[0] = m;
	
	for (int i = 1; i < 14; ++i){
		m.p = P[i-1].p + R[i-1].p;
		m.s =  P[i-1].s + R[i-1].s;
		m.r = P[i-1].r + R[i-1].r;
		if (P[i-1].S + R[i-1].S < R[i-1].S + P[i-1].S) m.S = P[i-1].S + R[i-1].S;
		else  m.S = R[i-1].S + P[i-1].S;
		P[i] = m;
		m.p = S[i-1].p + R[i-1].p;
		m.s =  S[i-1].s + R[i-1].s;
		m.r = S[i-1].r + R[i-1].r;
		if (S[i-1].S + R[i-1].S < R[i-1].S + S[i-1].S) m.S = S[i-1].S + R[i-1].S;
		else  m.S = R[i-1].S + S[i-1].S;
		R[i] = m;
		m.p = P[i-1].p + S[i-1].p;
		m.s =  P[i-1].s + S[i-1].s;
		m.r = P[i-1].r + S[i-1].r;
		if (P[i-1].S + S[i-1].S < S[i-1].S + P[i-1].S) m.S = P[i-1].S + S[i-1].S;
		else  m.S = S[i-1].S + P[i-1].S;
		S[i] = m;
	}
	
	//cout << R[1].p << " " << R[1].s << " " << R[1].r << endl;
	
	//cout << R[2].p << " " << R[2].s << " " << R[2].r << endl;
	
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t){
		cout << "Case " << "#" << t << ": ";
		cin >> n >> r >> p >> s;
		
		Move M;
		M.p = -1;
		
		if (P[n].p == p && P[n].r == r && P[n].s == s){
			M = compare(M, P[n]);
		}
		
		if (R[n].p == p && R[n].r == r && R[n].s == s){
			M = compare(M, R[n]);
		}
		
		if (S[n].p == p && S[n].r == r && S[n].s == s){
			M = compare(M, S[n]);
		}
		
		if (M.p != -1) cout << M.S << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
		
}
