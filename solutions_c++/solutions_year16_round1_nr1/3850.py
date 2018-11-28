#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string process(string s){

	stringstream ss;
	ss << s[0];
	string ret;
	ss >> ret;
	for (int i = 1 ; i < s.size() ; i++){
		//cout << ret << endl;
		if (s[i] >= ret[0]){
			ret = s[i] + ret;
			
		} else {
			ret += s[i];
		}
	}
	return ret;
}

int main(){
	int T;
	cin >> T;
	string s;
	for (int t = 1 ; t <= T ; t++){		
		cin >> s;
		//cout << s << endl;
		cout << "Case #" << t << ": " << process(s) << endl;
	}

	return 0;
}
