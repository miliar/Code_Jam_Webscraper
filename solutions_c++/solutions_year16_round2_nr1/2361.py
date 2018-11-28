#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	char identifier [10] = {'Z', 'O', 'W', 'H', 'U', 'V', 'X', 'S', 'G', 'N'};
	string name [10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int order [10] = {0,2,6,4,8,7,1,3,5,9};
	
	int T;

	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		vector <int> number;
		for (int i = 0; S.length() != 0; i++) 	{
			while ( S.find(identifier[order[i]]) != string::npos ) {
				number.push_back(order[i]);
				for (int j = 0; j < name[order[i]].length(); j++) {
					//cout << S << '\n';
					S.erase( S.find( name[order[i]][j] ),1 );
				}
			}
		}
		
		sort(number.begin(), number.end());
		cout << "Case #" << t << ": ";
		for (int i = 0; i < number.size(); i++) {
			cout << number[i];
		}
		cout << '\n';
	}
}
