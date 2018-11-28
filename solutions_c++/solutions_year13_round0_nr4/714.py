#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> sol;
vector<vector<int> > key;
vector<int> need,start;
set<int> S;
int C;

int solve(int m){
	//cout << "*" << m <<  " " << (1<<C)-1 << endl;
	if(m==(1<<C)-1)return 1; 
	if(S.find(m) != S.end())return 0; S.insert(m);
	multiset<int> keys(start.begin(),start.end()); 
	for(int i=0;i<C;i++) if(m & (1<<i)){
		keys.insert(key[i].begin(),key[i].end());
	} 
	for(int i=0;i<C;i++) if(m & (1<<i)) 
		keys.erase(keys.find(need[i]));
	//for(auto it = keys.begin();it!=keys.end();it++) cout << (*it) << " "; cout << endl;
	for(int i=0;i<C;i++) if( ! (m & (1<<i))){
		if(keys.find(need[i]) != keys.end())
			if(solve(m | (1<<i)) == 1){ sol.push_back(i+1); return 1; } 
	}
	return 0;
}

int main(void){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		sol.clear();
		S.clear();
		cout << "Case #"<<t<<":";
		int K;
		cin >> K >> C;
		key.resize(C);
		need.resize(C);
		start.resize(K);
		for(int i=0;i<K;i++) cin >> start[i];
		for(int i=0;i<C;i++){
			cin >> need[i] >> K;
			key[i].resize(K);
			for(int j=0;j<K;j++) cin >> key[i][j];
		}
		if(solve(0) == 1){
			reverse(sol.begin(),sol.end());
			for(int i=0;i<sol.size();i++)cout << " " << sol[i];
			cout << endl;
		}
		else cout << " IMPOSSIBLE" << endl;
	}
}