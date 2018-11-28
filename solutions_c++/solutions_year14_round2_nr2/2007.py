#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; ++i){
		int A,B,K,ans=0;
		cin >> A >> B >> K;
		for(int j=0; j<A; ++j){
			for(int k=0; k<B; ++k){
				if((j&k)<K){
					//cout << j << ' ' << k << endl;
					++ans;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
