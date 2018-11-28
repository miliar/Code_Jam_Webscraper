#include <iostream>
using namespace std;

int main(){
	int T, tt;
	int K, C, S;
	cin >> T;
	for(tt=1;tt<=T;tt++){
		cout << "Case #" << tt << ": ";
		cin >> K >> C >> S;
		if( S*C < K ){cout << "IMPOSSIBLE\n"; continue;}//riscrivi meglio, è vero???
		if(S==K){
			for(int i=1;i<=K;i++){
				if(i<K)cout << i << " ";
				else cout << i << endl;
			} continue;
		}
	}
	return 0;
}
