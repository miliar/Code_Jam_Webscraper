#include <iostream>
#include <string>
# include <algorithm>
#include <vector>

using namespace std;

int main() {
	int t;
	vector<string> inp;
	string str, newStr, newStr1, newStr2;
	char ch;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin >> str;
		newStr.clear();
		newStr1.clear();
		newStr2.clear();
		for (int j =0; j<str.length(); j++){
			ch = str[j];
			newStr1 = ch+newStr;
			newStr2 = newStr+ch;
			newStr = (newStr1 < newStr2)?newStr2:newStr1;
			//cout << newStr << " ";
		}
		cout <<"Case #"<<i<<": "<< newStr <<endl;
	}
	return 0;
}
