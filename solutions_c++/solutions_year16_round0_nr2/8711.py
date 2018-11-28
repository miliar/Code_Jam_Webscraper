#include<iostream>

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	string str;
	for(int q=1; q<=t; q++){
		cin >> str;

		char current;
		int invert = 0;
		current = str[0];
		for(int i=1; i<str.size(); i++){
			if (str[i] != current){
				invert++;
				current = str[i];
			}else
				continue;
		}
		if (str[str.size()-1] == '-')
			cout << "Case #" << q << ": " << (invert+1) << "\n";
		else
			cout << "Case #" << q << ": " << invert << "\n";
	}
	return 0;
}