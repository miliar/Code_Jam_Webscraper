#include <iostream>
#include <string>
#include <queue>

using namespace std;


int negative(int a) {
	if (a <= 4) return a + 4;
	return a -4;
}


int multiply(int a, int b) {
	if (a == 1) return b;
	if (b == 1) return a;
	if (a > 4 && b > 4) return multiply(a-4, b-4);
	if (a > 4 && b <= 4) return negative(multiply(a-4, b));
	if (a <= 4 && b > 4) return negative(multiply(a, b-4));
	if (a == 2 && b == 2) return 5;
	if (a == 2 && b == 3) return 4;
	if (a == 2 && b == 4) return 7;
	if (a == 3 && b == 2) return 8;
	if (a == 3 && b == 3) return 5;
	if (a == 3 && b == 4) return 2;
	if (a == 4 && b == 2) return 3;
	if (a == 4 && b == 3) return 6;
	if (a == 4 && b == 4) return 5;
}


bool isPossible(int pos, vector<int>& input) {
	int sum = 1;
	for (int i=pos; i<input.size(); ++i) {
		sum = multiply(sum, input[i]);	
	}
	return sum == 4;
}

int main () {
	int numTestCases;
	cin >> numTestCases;
	for (int it=0; it<numTestCases; ++it) {
		int l, mult;
		cin >> l >> mult;
		vector<int> input;
		string temp;
		cin >> temp;
		for (int i=0; i<temp.length(); ++i) {
			char c = temp[i];
			if (c == '1') {input.push_back(1);}
			if (c == 'i') {input.push_back(2);}
			if (c == 'j') {input.push_back(3);}
			if (c == 'k') {input.push_back(4);}
		}
		for (int j=0; j<mult-1; ++j) {
			for (int i=0; i<l; ++i) {
				input.push_back(input[i]);			
			}
		}
		vector<int> results;
		int sum = 1;
		for (int i=input.size()-1; i>=0; --i) {
			sum = multiply(input[i], sum);
			results.push_back(sum);	
		}

		int possible = 0;
		int start = 1;
		for (int pos1=0; pos1<input.size()-2; ++pos1) {
			start = multiply(start, input[pos1]);
			if (start == 2) {
				int middle = 1;
				for (int pos2=pos1+1; pos2<input.size()-1; ++pos2) {
					middle = multiply(middle, input[pos2]);
					if (middle == 3 && results[input.size() - (pos2+2)] == 4) {
						possible = 1;
						break;				
					}
				}
			}
			if (possible == 1) break;				
		}
		if (possible == 1) {
			cout << "Case #" << (it+1) << ": " << "YES" << endl;
		} else {
			cout << "Case #" << (it+1) << ": " << "NO" << endl;
		} 
	}
}
