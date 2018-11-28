#include<bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		string S;
		cin >> S;
		int count = 0;
		for(int j = 1; j < S.size(); j++){
			if(S[j] != S[j - 1])
				count++;
		}
		if(S[S.size()-1] == '-')
			count++;
		cout << "Case #" << i+1 <<": "<< count << endl;
	} 
}