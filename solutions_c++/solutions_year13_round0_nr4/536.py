#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int keys[1 << 20][210];
int vis[1 << 20];
int ans[210];
int chest[210];
vector<int> chest_keys[210];

bool solve(int mask, int N, int t, int pos){
	if(pos == N)
		return true;
		
	vis[mask] = t;
		
	for(int i = 0; i < N; i++){
		if(mask & (1 << i)) continue;
		
		int nmask = mask | (1 << i);
		if(!keys[mask][chest[i]] || vis[nmask] == t) continue;
		
		memcpy(keys[nmask], keys[mask], sizeof(keys[mask]));
		keys[nmask][chest[i]]--;
		
		for(int k = 0; k < chest_keys[i].size(); k++){
			keys[nmask][chest_keys[i][k]]++;
		}
		
		ans[pos] = i;
		
		if(solve(nmask, N, t, pos+1))
			return true;
	}
	
	return false;
}

int main(){
	int T, K, N;
	
	cin >> T;
	
	for(int t = 1; t <= T; t++){
		cin >> K >> N;
		
		memset(keys[0], 0, sizeof(keys[0]));
			
		for(int i = 0; i < K; i++){
			int key;
			cin >> key;
			keys[0][key]++;
		}
		
		for(int i = 0; i < N; i++){
			int Ti, Ki;
			cin >> Ti >> Ki;
			chest[i] = Ti;
			
			chest_keys[i].clear();
			
			for(int k = 0; k < Ki; k++){
				int key;
				cin >> key;
				chest_keys[i].push_back(key);
			}
		}
		
		cout << "Case #" << t << ":";
		
		if(solve(0, N, t, 0)){
			for(int i = 0; i < N; i++){
				cout << " " << ans[i]+1;
			}
			cout << "\n";
		}
		else
			cout << " IMPOSSIBLE\n";
	}		
}
