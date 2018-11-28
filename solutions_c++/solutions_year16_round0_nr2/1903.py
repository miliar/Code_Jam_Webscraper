#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;
int T;
string S;

int main(){
	cin >> T;
	for(int i=0; i<T; i++){
		cin >> S;
		S += "+";
		int count = 0;
		for(int j = 0; j < S.length()-1; j ++){
			if(S[j] != S[j+1])
				count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
}