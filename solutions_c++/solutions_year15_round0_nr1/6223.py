#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;

	int cs = 1;
	while(t--) {
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		int standing = 0, more = 0;
		for(int i=0;i<s.length();i++) {
			int x = (s[i] - '0');
			if(i==0) {
				standing = x;
			} else if(x > 0) {
				if(standing >= i) {
					standing += x;
				} else {
					more += (i - standing);
					standing += (i - standing);
					standing += x;
				}
			}
		}

		cout<<"Case #"<<cs<<": "<<more<<endl;
		cs++;
	}
}