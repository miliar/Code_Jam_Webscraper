#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		string s;
		cin>>s;
		bool up=0;
		int r=0;
		for(int j=s.size()-1;j>-1;j--) { 
			if((s[j]=='-'&&up==0) || (s[j]=='+'&&up==1))
				r++,up^=1;
		}
		cout<<"Case #"<<i<<": "<<r<<endl;;
	}
	return 0;
}

