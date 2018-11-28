#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		string s;
		cin >> s;
		int count = 0;
		for(int i = s.size() - 1; i >= 0; i--){
			if(i == 0){
				if(s[i] == '-')
					count++;
			}
			else{
				if(s[i] == '-' && s[i - 1] == '+'){
					count++;
					for(int j = i; j >= 0; j--){
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				}
				
			}
			
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	
	return 0;
}