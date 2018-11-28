#include<bits/stdc++.h>
using namespace std;
typedef long long LL;


vector<LL> solve(int K, int C, int S) {
	if(C * S < K) return vector<LL>();
	vector<LL> ans;
	
	for(int i=0; i<S; i++) {
		LL data = 0;
		if( C*i >= K ) break;
		for(int j=C*i ; j<min(C*(i+1), K); j++) {
			data *= (LL)K;
			data += (LL)j;
		}
		ans.push_back(data+1); 
	}
	return ans;
	
}



int main() {
	int T;
	cin >> T;
	for(int i=0; i<T; i++ ) {
		int K,C,S;
		cin >> K >> C >> S;
		vector<LL> ans = solve(K,C,S);
		cout << "Case #" << i+1 <<  ": ";
		if(ans.size() == 0) cout << "IMPOSSIBLE" << endl;
		else  {
			for(int j=0; j<ans.size(); j++) {
				cout << ans[j] ;
				if(j + 1 == ans.size())
					cout << endl;
				else cout << " ";
			}
			
		}
		
	}
	
	return 0;
}

