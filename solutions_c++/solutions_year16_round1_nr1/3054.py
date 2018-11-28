#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream out;
	out.open("A-large-output");

	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		string S;
		cin >> S;
		string result = "";
		out << "Case #" << i << ": ";
		result = S[0];
		for(int j = 1; j < S.size(); j++){
			if(S[j] >= result[0])
				result = S[j] + result;
			else
				result += S[j];
		}
		out << result << '\n';
	}
	out.close();
}