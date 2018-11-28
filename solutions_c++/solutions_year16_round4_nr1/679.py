#include "bits/stdc++.h"
using namespace std;
int t;
int n , r , p , s;
vector < char > v;
bool ok;
map < char , int > mp;
char win(char a , char b){
	if(mp[a] == (mp[b] + 1) % 3){
		return a;
	}
	return b;
}
bool solve(){
	vector < char > v = ::v;
	while(v.size() > 1){
		vector < char > tmp;
		tmp.clear();
		for(int i = 0 ; i < v.size() ; i += 2){
			if(v[i] == v[i + 1]){
				return 0;
			}
			tmp.emplace_back(win(v[i] , v[i + 1]));
		}
		v = tmp;
	}
	return 1;
}
int main(){
	mp.clear();
	mp['R'] = 0;
	mp['P'] = 1;
	mp['S'] = 2;
	cin >> t;
	for(int tc = 1 ; tc <= t ; ++tc){
		cout << "Case #" << tc << ": ";
		cin >> n >> r >> p >> s;
		v.clear();
		for(int i = 1 ; i <= r ; ++i){
			v.emplace_back('R');
		}
		for(int i = 1 ; i <= p ; ++i){
			v.emplace_back('P');
		}
		for(int i = 1 ; i <= s ; ++i){
			v.emplace_back('S');
		}
		sort(v.begin() , v.end());
		ok = 0;
		do{
			if(solve()){
				ok = 1;
				break;
			}
		}while(next_permutation(v.begin() , v.end()));
		if(ok){
			for(char c : v){
				cout << c;
			}
		}
		else{
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}
