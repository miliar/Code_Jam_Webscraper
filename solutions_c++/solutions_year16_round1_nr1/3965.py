#include <iostream>
#include <string>
using namespace std;
string shift(char letter, string s) {
	string newString = "";
	if(s.length() > 0) {
		if(letter >= s[0]) {
			newString.append(1,letter);
			newString.append(s);
		}
		else {
			newString.append(s);
			newString.append(1,letter);
		}
	}
	else 
	{
		newString.append(1,letter);
	}
	//cout<<"ewString: "<<newString<<endl;
	return newString;
}
int main() {
	// your code goes here
	int T;
	cin>>T;
	string s;
	
	for(int i = 0 ; i<T;i++) {
		cin>>s;
		string output = "";
		for(int j = 0; j< s.length();j++) {
			
			output = shift(s[j],output);
		}
		cout<<"Case #"<<i+1<<": "<<output<<endl;
	}
	
	return 0;
}