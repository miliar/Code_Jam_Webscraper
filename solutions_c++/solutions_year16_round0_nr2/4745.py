#include <iostream>
#include <string>
using namespace std;


string reduce(string s){
	char last = s[0];
	string ret = s.substr(0,1);
	for(int i=1; i<s.size(); i++){
		if(s[i] != last){
			ret += s[i];
			last = s[i];
		}
			
	}
	return ret;
}


int main() {
	// your code goes here
		int t;
		cin>>t;
		int ans = 0;
		for(int i=0; i<t; i++){
			string s;
			cin>>s;
			string ss = reduce(s);
			
		if(ss[ss.size()-1] == '-'){
			ans = ss.size();
		}
		else{
			ans = ss.size()-1;
		}
		
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}