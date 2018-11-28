#include <bits/stdc++.h>

using namespace std;

string s;

int main(int argc, char **argv){
	std::ios::sync_with_stdio(false);

	int tests;
	char c = 'p';
	int count = 0;

	cin >> tests;
	for(int i = 0 ; i < tests ; i++){
		c = 'p';
		count = 0;

		cin >> s;
		for(int j = s.length()-1 ; j >= 0 ; j--){
			if(c == 'p'){
				if(s[j] == '-'){
					c = 'm';
					count++;
				}
			}
			else{
				if(s[j] == '+'){
					c = 'p';
					count++;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;

		s.clear();
	}

	return 0;
}