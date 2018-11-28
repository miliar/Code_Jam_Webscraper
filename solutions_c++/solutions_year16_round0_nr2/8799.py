#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	int t, flips, lpos;
	string str, sub;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin>>str;
		sub.clear();
		flips = 0;
		if (str == "-")
			cout <<"Case #"<<i<<": 1"<<endl;
		else if (str == "+")
			cout <<"Case #"<<i<<": 0"<<endl;
		else	{
			for (int j =0; j<str.length()-1; j++) {
				sub.clear();
				sub.append(str,j,2);
				if (sub == "-+" || sub == "+-")
					flips++;
			}
			//cout << sub <<endl;
			if (sub[1] == '-')
					flips++;
			cout <<"Case #"<<i<<": "<<flips<<endl;		
		}
	}
	return 0;
}
