
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------

#ifdef cin fin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif



int main() {
	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while(t--){
		cout << "Case #" << z++ << ": ";
		string s;
		int k;
		cin>>s >> k;
		
		int ans = 0, n = s.size();
		for (int i = 0 ; i < s.size(); i++){
			if(s[i] == '-'){
				if (n - i < k) {
					ans = -1;
					break;
				}
				ans++;
				for(int j = i; j < i + k; j++) s[j] = (s[j] == '+') ? '-' : '+';
			}
		}
		if(ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}