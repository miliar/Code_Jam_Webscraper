#include <iostream>
#include <vector>
using namespace std;

int main(){
	//freopen("B2.in", "r", stdin);
	//freopen("myoutB2.out", "w", stdout);
	int T;
	cin >> T;
	
	for(int k = 1; k <= T; ++k){
		string s;
		cin >> s;
		int counter = 0;
		for(int i = s.length()-1; i >= 0; --i){
			if(s[i] == '-'){
				counter ++;
				for(int j = i; j >= 0; --j){
					if(s[j] == '-'){
						s[j] = '+';
					}
					else if(s[j] == '+'){
						s[j] = '-';
					}
				}
			}
		}
		
		cout << "Case #" << k << ": " << counter<<endl;
	}
	return 0;
}
