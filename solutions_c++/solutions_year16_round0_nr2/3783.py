#include <iostream>
using namespace std;

// function to count breakpoints (number of places where we have a + next to a -)
int time_flip_pancakes(string &S) {
	char c = S[0];
	int i = 0;
	int k = 0;
	while(i < S.size()) {
		if(c != S[i]) {
			k++;
			if(c == '+')
				c = '-';
			else
				c = '+';
		}
		i++;
	}
	if(c == '-')
		k++;
	return k;
}

int main() {
	int T,i,N;
	string S;
	cin >> T;
	for(i = 0; i < T; i++) {
		cin >> S;
		// flip pancakes
		N = time_flip_pancakes(S);
		cout << "Case #" << i+1 << ": " << N << endl;
	}
	return 0;
}