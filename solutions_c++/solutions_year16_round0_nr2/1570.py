#include <iostream>
#include <string>

using namespace std;

int getNumber(const string& s)
{
	if (s=="+") return 0;
	if (s=="-") return 1;
	return 1+getNumber(string(s.begin()+1, s.end()));
}

string getBiNumber(string& cake)
{
	string number;
	number.clear();
	for (int i=0; i<cake.length(); ++i)
	{
		if (cake[i]=='+' && (number.empty() || number[number.length() - 1]!='+')) {
			number.push_back('+');
		}
		if (cake[i]=='-' && (number.empty() || number[number.length() - 1]!='-')) {
			number.push_back('-');
		}
	}
	return number;
}

int main() {
	int t;
	cin >> t;
	string cake;
	getline(cin, cake, '\n');
	for (int i=0; i<t; ++i) {
		string cake;
		getline(cin, cake, '\n');
		string number = getBiNumber(cake);
		cout << "Case #" << i+1 << ": " << getNumber(number) << endl;

	}
}