#include <bits/stdc++.h>
#define EPS 1e-11
#define LB 1e11
#define EL cerr << endl;
#define DB(x) cerr << "#" << (#x) << ": " << (x) << " ";
#define DBL(x) cerr << "#" << (#x) << ": " << (x) << endl;
#define PR(x) cout << (x) << endl

#define X first
#define Y second
#define PB push_back
#define SQ(x) ((x)*(x)) 

using namespace std; typedef string string;
typedef unsigned long long ull; typedef long double ld;
typedef long long ll;         typedef pair<int, int> ii;
typedef pair<int, ii> iii;    typedef vector<int> vi;
typedef vector<ii> vii;       typedef vector<vi> vvi;
typedef vector<ll> vll;       typedef pair<string, string> ss;
const static int MX = 1010;

int C[30], R[10], n;
string S, N[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void r(int x){
	R[x]++;
	for(int i = 0; i < N[x].size(); i++) C[N[x][i] - 'A']--;
}

int main() {
	int tc, i, j, t = 1;
	cin >> tc;
	while(tc--){
		memset(C, 0, sizeof C);
		memset(R, 0, sizeof R);
		cin >> S;
		n = S.size();
		for(i = 0; i < n; i++){
			C[S[i] - 'A']++;
		}
		
		while(C['Z'-'A'])r(0);
		while(C['W'-'A'])r(2);
		while(C['U'-'A'])r(4);
		while(C['X'-'A'])r(6);
		while(C['R'-'A'])r(3);
		while(C['H'-'A'])r(8);
		while(C['O'-'A'])r(1);
		while(C['F'-'A'])r(5);
		while(C['V'-'A'])r(7);
		while(C['N'-'A'])r(9);
		
		cout << "Case #" << (t++) << ": ";
		for(i = 0; i < 10; i++){
			while(R[i]) {cout << i; R[i]--;}
		}
		cout << endl;
	}
	
}
