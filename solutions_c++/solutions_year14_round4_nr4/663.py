#include<iostream> 
#include <cstring>
#include <cstdio>
#include <set>
#include <vector>
#include<queue> 
using namespace std; 
#define MOD 100000007
#define ll long long
vector <string> ve[1005];
set <string> se[1005];
string s;
int _pow(int x, int k){
	int res = 1;
	while(k--){
		res *= x;
	}
	return res;
}
string str;
int main() { 
	int T, cas = 1, n, m;
	cin >> T;
	while(cas <= T){
		printf("Case #%d: ", cas++);
		
		cin >> n >> m;	
		for(int i = 0; i < n; i++){
			cin >> s;
			str = "";
			ve[i].clear();
			for(int j = 0; j < s.length(); j++){
				str += s[j];
				ve[i].push_back(str);
			}
		}
		ll max_c = 0, cc = 0;
		for(int i = 0; i < _pow(m, n); i++){
			int st = i;
			for(int j = 0; j < m; j++) se[j].clear();
			for(int j = 0; j < n; j++){
				int t = st % m; st /= m;
				for(int k = 0; k < ve[j].size(); k++){
					se[t].insert(ve[j][k]);
				}
			}
			ll c = 0;
			bool flag = false;
			for(int j = 0; j < m; j++){
				if(se[j].size() == 0) flag = true;
				c += se[j].size()+1;
			}
			if(flag) continue;
			if(max_c < c){
				max_c = c; cc = 0;
			}
			if(max_c == c){
				cc++; cc %= MOD;
			}
		}
		cout << max_c << " " << cc << endl;
		
	}
}
