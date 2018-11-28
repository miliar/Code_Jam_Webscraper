#include <bits/stdc++.h>
using namespace std;
#define all(v) v.begin(),v.end()
#define allr(v) v.rbegin(),v.rend()
#define forn(i,k,n) for(int i = k; i < n; ++i)
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

int main(){
	ios_base::sync_with_stdio(false);	//cin.tie(0);
	ifstream ifs("B-large.in");
  ofstream ofs("B-large_output.txt");
	int t = 1, tcase = 1;
	//cin >> t;
	ifs >> t;

	while(t--){
		int n;
		//cin >> n;
		ifs >> n;

		int vec[2*n-1][n], men = 0;
		forn(i,0,2*n-1){
			forn(j,0,n) ifs >> vec[i][j], men = max(men, vec[i][j]);
		}

		vi vfr(men+1,0);
		forn(i,0,2*n-1){
			forn(j,0,n) ++vfr[vec[i][j]];
		}

		vi v;
		forn(i,0,men+1) if(vfr[i] & 1) v.push_back(i);

		int size = v.size();
//		cout << "Case #" << tcase++ << ": ";
//		forn(i,0,size-1) cout << v[i] << " ";
//		cout << v[size-1] << "\n";
		ofs << "Case #" << tcase++ << ": ";
		forn(i,0,size-1) ofs << v[i] << " ";
		ofs << v[size-1] << "\n";
	}
	return 0;
}
