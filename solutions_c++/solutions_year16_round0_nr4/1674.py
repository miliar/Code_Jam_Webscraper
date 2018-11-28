#include<iostream>
using namespace std;

int main(){
	int T,K,C,S;

	cin >> T;
	int I = T;
	while(T--){
		cin >> K >> C >> S;

		cout << "Case #" << I-T << ": ";
		for(int i=1;i<=K;i++)
			cout << i << " ";
		cout << endl;
	}
	return 0;
}