/*	Title : Standing Ovation
	Link : https://code.google.com/codejam/contest/6224486/dashboard
*/

#include<iostream>

using namespace std;

int main () {
	int T,smax,total,required;
	int input[1001];
	char array[1010];
	cin >> T;
	for (int i=0; i < T; i++) {
		cin >> smax;
		cin >> array;
		//cout <<"The smax is :" << smax << endl;
		//cout << array<<endl;
		for (int j=0; j <= smax; j++) {
			input[j] = (int) array[j] - 48;
		}
		/*for ( int j=0; j <= smax; j++) {
			cout << input[j] << ' ';
		}
		cout << endl;
		*/
		total = input[0];
		required = 0;
		for (int j=1; j <= smax; j++) {
			//cout << "j = " << j << "  input = " << input[j];
			if (total >= j) {
				total += input[j];
				//cout << "  total = " << total;
			}
			else {
				required += 1;
				total += (input[j] + 1);
				//cout << "  required = " << required << "  total = " << total;
			}
			//cout << endl;
		}
		if (i != 0) {
			cout <<endl;
		}
		cout << "Case #" << (i+1) << ": " << required;
	}
	return 0;
}
