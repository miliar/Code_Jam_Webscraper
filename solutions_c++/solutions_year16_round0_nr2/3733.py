#include <iostream>
#include <map>
using namespace std;
map<char, char> M;

int steps(string s, char c){

	// cout<<"called for "<<s<<" on "<<c<<endl;

	int n = s.size(), j = n-1;
	if(n == 1){
		return s[0] == c ? 0 : 1;
	}
	while(j >= 0 && s[j] == c) j--;
	if(j < 0) return 0;
	n = steps(s.substr(0, j+1), M[c]);
	// cout<<"ans is "<<n+1<<endl;
	return n + 1;
}

int main(){

	int t;
	string s;
	cin>>t;

	M['+'] = '-';
	M['-'] = '+';
	
	for(int i = 1; i <= t; i++){
		cin>>s;
		cout<<"Case #"<<i<<": "<<steps(s, '+')<<endl;
	}
}