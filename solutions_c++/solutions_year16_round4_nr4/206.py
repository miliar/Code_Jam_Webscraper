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
typedef vector <bool> VB;
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

int n;
VVI M;
int k;

bool check2 (int z, VI &v, VB &b){
	if (z == n) return true;
	bool found = false;
	for (int i = 0; i < n; ++i){
		if (!b[i] && M[v[z]][i]){
			found = true;
			b[i] = true;
			if (!check2(z+1, v, b)) return false;
			b[i] = false;
		}
	}
	return found;
}	

bool check (){
	VI v(n);
	for (int i = 0; i < n; ++i) v[i] = i;
	do{
		VB b(n, false);
		if (!check2(0, v, b)) return false;
	} while(next_permutation(v.begin(), v.end()));
	return true;
}

void Backtracking(int z1, int z2, int m){
	if (z1 == n){
		/*for (int i = 0; i < n; ++i){
			for (int j = 0; j < n; ++j){
				cout << M[i][j];
			}
			cout << endl;
		}
		cout << endl;*/
		if (check()) k = min(m,k);
		return;
	}
	
	if (m >= k) return;
	
	int newz1 = z1, newz2 = z2+1;
	if (newz2 == n){
		newz2 = 0;
		++newz1;
	}
	
	if (M[z1][z2] == 0){
		Backtracking(newz1, newz2, m);
		M[z1][z2] = 1;
		Backtracking(newz1, newz2, m+1);
		M[z1][z2] = 0;
	}
	else Backtracking(newz1, newz2, m);
	
}

int main(){
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		cout << "Case #" << t << ": ";
		cin >> n;
		M = VVI(n, VI(n));
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < n; ++j){
				char c;
				cin >> c;
				if (c == '0') M[i][j] = 0;
				else M[i][j] = 1;
			}
		}
		k = 1000000;
		Backtracking(0,0,0);
		cout << k << endl;
	}
    
}
