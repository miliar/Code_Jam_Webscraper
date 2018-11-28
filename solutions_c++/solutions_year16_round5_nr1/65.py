#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;



int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		//int n; cin >> n;
		string s; cin >> s;
		stack<char> st;
		int n = s.length();
		int ans = 0;
		for (int i = 0; i < n; i++){
			if (st.empty()){
				st.push(s[i]);
				continue;
			}
			else if (st.top() == s[i]){// && st.size() < n-i){
				st.pop();
				ans +=2;
			}
			else if (st.size() < n-i){
				st.push(s[i]);
			}
			else{
				st.pop();
				ans += 1;
			}
		}
		cout << "Case #" << zz << ": " << (5*ans) << endl;
	}
	
	return 0;
}
