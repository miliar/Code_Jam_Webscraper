#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> digitCheck(10, 0);

bool isSolution(int n, int last);
void fill(unsigned long long int n);

int main() {
	unsigned long long int last = 0;
	unsigned long long int N, T, current;
	bool solved;
	
	cin >> T;

	for(unsigned long long int i = 0; i < T; i++) {
		cin >> N;
		solved = true;
		current = 0;

		while(!isSolution(9, 1)) {
			current += N;
		
			if(current == last) {
				solved = false;
				break; 
			}

			fill(current);

			last = current;
		}

		cout << "Case #" << (i+1) << ": ";

		if(solved) {
			cout << last << endl;
		}
		else {
			cout << "INSOMNIA" << endl;
		}

		digitCheck.assign(10, 0);
	}

	return 0;
}

bool isSolution(int n, int last) {
	if(n == 0) {
		return (digitCheck[n] & last);
	}

	return isSolution(n-1, (digitCheck[n] & last));
}

void fill(unsigned long long int n) {
	while(n) {
		digitCheck[n%10] = 1;
		n /= 10;
	}
}