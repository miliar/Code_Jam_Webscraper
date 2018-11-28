#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

vector<char> pancake(string s) {
	vector<char>pancakes;
	for each(char num in s) {
		pancakes.push_back(num);
	}
	return pancakes;
}

int main() {
	
	string s;
	vector<char> pancakes;
	bool order = false;
	int counter = 0,t;
	cin >> t;

	for (int m = 1; m <= t; ++m) {
		cin >> s;
	pancakes = pancake(s);
	counter = 0;
	order = false;

	do {

		for (int i = pancakes.size()-1; i >= 0; i--)
		{
			if (pancakes[i] == '-') {
				for (int j = 0; j <= i; j++) {
					if (pancakes[j] == '-')
						pancakes[j] = '+';
					else
						pancakes[j] = '-';
				}
				order = false;
				counter++;
				break;
				
			}
			else 
				order = true;
		}
		
	} while (!order);
	
	cout << "Case #" << m << ": "<< counter << endl;
	}

	system("pause>0");
	return 0;
}




