#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int k = 0; k < T; k++) {
	int N = 0, i;
	std::string S;
	cin >> S;
	for(i = 0; i < S.length(); i++) {
		if(S[i] == '-') continue;
		else break;
	}
	if(i > 0)  N = 1;
	for(; i < S.length(); i++) {
		if(S[i] == '-') { 
		    N = N+2;
		    int j = i+1;
		    for(; j < S.length(); j++) {
		        if(S[j] == '-') continue;
		        else break;
		    }
		    i = j;
		}
	}
	cout << N << endl;
	}
return 0;
}
