#include <iostream>

using namespace std;

long long getVariedNum(int n, int k, int c){
	if(k == 1){
		return 1;
	}
	long long x = 0;
	for(int i = n * c; i < (n+1)*c; i++){
		x *= k;
		if(i >= k){
			x++;
		}else{
			x += i;
		}
	}
	return x+1;
}

int main(){
	int T, K, C, S;
	cin >> T;
	for(int k = 1; k <=T; k++){
		cout << "Case #" << k << ": ";
		cin >> K >> C >> S;
		if(K+(C-1)/C>S){
				cout << "IMPOSSIBLE" << endl;	
		}else{
			for(int n = 0; n < (K+(C-1))/C; n++){
				if(n == 0){
					cout << getVariedNum(n, K, C); 
				}else{
					cout << " " << getVariedNum(n, K, C); 
				}
			}
			cout << endl;
		}
	}
	return 0;
}
