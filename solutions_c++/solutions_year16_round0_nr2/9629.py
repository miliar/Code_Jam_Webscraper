#include<iostream>
#include<string>
using namespace std;



int main() {
	int T;
	cin >> T;
	
	for(int TCASE=1;TCASE<=T;TCASE++) {
		string s;
		cin >> s;
		s+="+";
		
		int result = 0;
		for(size_t i=0;i+1<s.size();i++)
			result += s[i+1] != s[i];
		
		cout << "Case #" << TCASE << ": " << result << '\n';
	}
	
	return 0;
}
























