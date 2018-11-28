#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	int cs = 1;
	while(T--) {
		string s;
		cin>>s;
		int n= s.length();
		string ne = "";
		ne += s[0];
	//	cout<<ne<<endl;
		
		for(int i=1;i<n;i++) {
	//		cout<<ne<<endl;
			if(s[i] >= ne[0]) ne = s[i] + ne;
			else ne = ne + s[i];
		}
		
		cout<<"Case #"<<cs++<<": "<<ne<<endl;
	}
	// your code goes here
	return 0;
}