//In the Name of Allah
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

const double eps = 1e-12;
typedef long long ll;
typedef pair<int, int> pii;
//#define For(i, a, b) for (int i = (a); i < (b); i++)
#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << err; while(1); }

int main () {
	//*
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	//*/

	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++){
		debug(tc);
		int n, x;
		cin >> n >> x;
		vector <int> v (n+1);
		vector <bool> u (n+1);
		v[0] = 0;
		u[0] = false;
		for (int i=1; i<=n; i++) {
			cin >> v[i];
			u[i] = false;
		}
		sort(v.begin(), v.end());
		int cnt = 0;
		for (int i = n; i>0; i--){
			if(u[i]) continue;
			cnt++;
			if(i==1) break;
			//u[i] = true;
			int j = i-1;
			while(1){
				if(u[j]) j--;
				else{
					if(v[i]+v[j] <= x) break;
					j--;
				}
			}
			if(j > 0) u[j] = true;
		}
		cout << "Case #" << tc << ": " << cnt << endl;
	}
	return 0;
}
/*
3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60

*/