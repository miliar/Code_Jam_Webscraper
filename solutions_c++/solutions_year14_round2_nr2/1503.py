#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	int K = 1;
	cin >> T;
	while(T--){
		int a , b , k;
		cin >> a >> b >> k;
		int ctr = 0;
		for(int i = 0 ; i < a ; ++i){
			for(int j = 0 ; j < b ; ++j){
				if((i & j) < k)ctr++;
			}
		}
		cout << "Case #" << K << ": " << ctr << endl;
		++K;
	}
	return 0;
}
