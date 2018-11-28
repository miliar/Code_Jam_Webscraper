#include <iostream>
using namespace std;
int main() {
	int T,j=1;
	cin >> T;
	while(T) {
		int length;
		cin >> length;
		string S;
		cin >> S;
		int sum = 0,
				total = 0,
				i = 1;
		while(total < length) {
			total += ((int)S[i-1]) - 48;
			if(total < i) {
				sum+=i-total;
				total+=i-total;
			}
			i++;
		}
		cout << "Case #" <<j << ": " << sum << endl; 
		T--; j++;
	}
}