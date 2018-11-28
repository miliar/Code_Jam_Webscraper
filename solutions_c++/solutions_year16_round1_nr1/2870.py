#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string S;

string getresult() {
	string left = "", right = "";
	int i = S.size()-1; 
	while(i >= 0) {
		int best = i;
		for(int j = i; j >= 0; j--)
			if(S[j] > S[best])
				best = j;
		left += S[best];
		for(int j = i; j > best; j--)
			right = S[j] + right;
		i = best - 1;
	}
	return left + right;
}

int main() {
	int tc;
	cin >> tc;
	for(int z = 1; z <= tc; z++) {
		cin >> S;
		cout << "Case #" << z  << ": " << getresult() << endl;
	}
}
