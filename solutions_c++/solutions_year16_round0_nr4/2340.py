#include<bits/stdc++.h>

using namespace std;

int main(){
	int T;
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for(int t=0;t<T;++t){
		int K,C,S;
		cin >> K >> C >> S;
		if(C*S<K){cout << "Case #" << t+1 << ": IMPOSSIBLE" << "\n";continue;}
		vector<long long> res;
		long long cntr=0;
		long long pos=0;
		for(int i=0;i<S;++i){
			for(int j=0;j<C;++j){
				if(cntr==K){res.push_back(pos);goto ende;}
				pos=pos*K+cntr;
				cntr++;
			}
			res.push_back(pos);
			pos=0;
		}
	ende:
		
		cout << "Case #" << t+1 << ": ";
		for(auto i:res)cout << i+1 << " ";
		cout << "\n";
	}
}
