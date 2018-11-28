#include <iostream>
using namespace std;
int main () {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		cin>>s;
		string result="";
		result = result+s[0];
		for(int j = 1; j < s.length(); ++j) {
			if (s[j] >= result [0]) {
				result = s[j] + result;
			}else {
				result = result + s[j];
			}
		}
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}


}