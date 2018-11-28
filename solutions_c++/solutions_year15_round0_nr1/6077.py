#include <iostream>
#include <string>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i){
		int s;
		cin >> s;
		string aud;
		cin >> aud; 
		unsigned int c = 0;
		unsigned int spolu = 0;
		for (unsigned int j = 0; j < aud.size(); j++){
			int a = aud[j];
			spolu += a - 48;
			if (spolu < j+1){
				++c;
				++spolu;
			}
		}
		cout << "Case #" << i << ": " << c << endl;
	}
	return 0;
}
