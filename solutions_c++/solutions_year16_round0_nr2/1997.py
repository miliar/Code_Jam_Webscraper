#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream out;
	out.open("B-large-output");

	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		string S;
		cin >> S;
		out << "Case #" << i << ": ";
		int count = 0;
		string newS;
		for(int j = 1; j < S.size(); j++){
			if(S[j] != S[j-1])
				newS += S[j];
		}
		if(S[0] == '+') count = newS.size() % 2 ? newS.size() + 1 : newS.size();
		else count = newS.size() % 2 ? newS.size() : newS.size() + 1;
		out << count << endl;
	}
	out.close();
}