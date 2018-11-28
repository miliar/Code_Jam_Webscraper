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
	ifstream ifs("A-small-attempt0.in");
  ofstream ofs("A-small-attempt0_output.txt");
	int t = 1, tcase = 1;
	//cin >> t;
	ifs >> t;

	while(t--){
		string s, word = "";
		//cin >> s;
		ifs >> s;

		int size = s.size();
		word += s[0];
		forn(i, 1, size){
			stringstream ss;
			string var;
			ss << s[i];
			ss >> var;
			if(s[i] >= word[0]) word = var + word;
			else word = word + var;
		}
		//cout << "Case #" << tcase++ << ": " << word << "\n";
		ofs << "Case #" << tcase++ << ": " << word << "\n";
	}
	return 0;
}
