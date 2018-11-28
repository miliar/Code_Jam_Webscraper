#include <iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	// your code goes here
	long long int t;
	cin>>t;
	for(int i = 1; i <= t; i++) {
		string s;

		cin>>s;

		
		/*etline(cin, s);
		cout<<"s is "<<s<<endl;
		if (s == "\n" || s == "") {
			i--;
			continue;
		}*/

		vector<char>out;
		vector<char>::iterator it;
		it = out.begin();
		out.insert(it, s[0]);

		for(int j = 1; j <= s.size(); j++) {

			if (s[j] > out[0]) {
				it = out.begin();
				it = out.insert(it, s[j]);
				//cout<<"sadd"<<endl;
			} else {
				
				out.push_back(s[j]);
			}
		}
		
		cout<<"Case #"<<i<<": ";
		for(int k = 0 ;k < out.size(); k++) {
			cout<<out[k];
		}
		cout<<endl;
		//s.clear();
	}
	return 0;
}