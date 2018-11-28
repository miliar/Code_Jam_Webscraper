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


double compute (VD &v, int k){
	int n = v.size();
	VVD M(n, VD(k+1, 0));
	M[0][0] = 1.0 - v[0];
	M[0][1] = v[0];
	for (int i = 1; i < n; ++i){
		for (int j = 0; j <= k; ++j){
			if (j == 0) M[i][j] = (1.0 - v[i])*M[i-1][j];
			else M[i][j] = v[i]*M[i-1][j-1] + (1.0 - v[i])*M[i-1][j];
		}
	}
	return M[n-1][k];		
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(6);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		cout << "Case #" << t << ": ";
		int n, k;
		cin >> n >> k;
		VD v(n);
		for (int i = 0; i < n; ++i) cin >> v[i];
		sort (v.begin(), v.end());
		double maxi = 0;
		for (int i = 0; i <= k; ++i){
			VD vv(0);
			for (int j = 0; j < i; ++j) vv.push_back(v[j]);
			for (int j = n-1; j >= n-k+i; --j) vv.push_back(v[j]);
			double a = compute(vv, k/2);
			maxi = max(a,maxi);
		}
		cout << maxi << endl;
	}
}
