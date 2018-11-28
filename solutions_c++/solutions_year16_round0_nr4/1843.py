#include <iostream>
#include <string>

int T, K, C, S;

using namespace std;
int main(){
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> K >> C >> S;
		cout << "Case #" << i+1 << ": " ;
		for(int j = 0; j < K; j++)
			cout << j+1 << " " ;
		cout << endl;
	}
}