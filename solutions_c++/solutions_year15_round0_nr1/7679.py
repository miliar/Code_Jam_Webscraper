#include <algorithm>
#include <iostream>

using namespace std;

int main(){
	int T; 
	cin >> T;

	for (int t = 0; t != T; t++){
		int S; 
		string Ss; 
		cin >> S >> Ss;
	
		unsigned int standing = 0;
		unsigned int needed = 0;
		for (unsigned int i = 0; i != Ss.length(); i++){
			if (i > standing){
				int extra = i - standing;
				needed += extra;
			   	standing += extra;	
			}
				standing += Ss[i]-'0';
		}
		
		cout << "Case #" << t+1 << ": " << needed << endl;
	}

	return 0;
}
