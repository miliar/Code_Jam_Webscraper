#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	string s;
	string lastWord;
	string tmp;
	char nextLetter;
	
	cin>>T;
	
	for(int i = 1; i <= T; i++) {
		cin>>s;
		lastWord = "";
		for(int j = 0; j <s.length(); j++) {
			if(j ==0 ) {
				lastWord += s[j];
			}
			else {
				if( lastWord[0] > s[j] ) {
					lastWord += s[j];
				}
				else {
					tmp = "";
					tmp += s[j];
					tmp += lastWord;
					lastWord = tmp;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<lastWord<<endl;
	}
}
