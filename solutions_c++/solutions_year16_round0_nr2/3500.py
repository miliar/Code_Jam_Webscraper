#include <iostream>
#include <string>
#include <map>

using namespace std;
map < string, long long > answers;

long long pancakes(string str){
	string sub = "";
	for (int j = 0; j < str.length() - 1; j++)
		sub += str[j];
	if (str == "+")
		return 0;
	else if (str == "-")
		return 1;
	else if (str[str.length() - 1] == '-' && str[str.length() - 2] == '+'){

		return pancakes(sub) + 2;
	}
	else return pancakes(sub);
}

int main()
{
	int t;
	cin >> t;
	string s;
	for (int i = 1; i <= t; i++){
		cin >> s;
		cout << "Case #" << i << ": " << pancakes(s) << endl;
	}
	return 0;
}