#include <iostream>
#include <string>
using namespace std;

int main(){
	int T, i, j;
	cin >> T;
	for(i = 0; i < T; i++){
		int moves = 0;
		string S;
		cin >> S;
  		for(j = 0; j < S.size() - 1 ; j++) {
  			if (S[j] != S[j + 1]) moves++;
  		}
  		if(S[S.size() - 1] == '-') moves++;
  		cout << "CASE #" << i + 1 << ": " << moves << endl;
	}
}