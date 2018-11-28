#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int kases;
	cin >> kases;
	for(int T=1; T<=kases; T++) {
		string input;
		cin >> input;
	
		int N = input.size(), n0=0, n1=0;
		for(int i=0; i<N; i++) {
			n0 = (input[i] == '-')?n0:n1+1;
			n1 = (input[i] == '+')?n1:n0+1;
		}
		
		cout << "Case #" << T << ": " << min(n1, n0+1) << endl;
	}
	
	return 0;
}