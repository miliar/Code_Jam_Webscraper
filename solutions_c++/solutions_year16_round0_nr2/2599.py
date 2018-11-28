#include <iostream>
#include <string>

using namespace std;

void flip(string& S, int pos){
	for(int i = 0; i <= pos; ++i){
		switch(S[i]){
			case '-':
				S[i] = '+';
				break;
			case '+':
				S[i] = '-';
				break;
		}
	}
}

int flip_pankakes(string& S){
	int n = S.size();
	int flips = 0;
	for(int i = n - 1; i >= 0; --i){
		if(S[i] == '-'){
			flip(S, i);
			flips++;
		}
	}
	return flips;
}

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		string S;
		cin >> S;
		cout << "Case #" << i << ": " << flip_pankakes(S) << endl;
	}
	return 0;
}

