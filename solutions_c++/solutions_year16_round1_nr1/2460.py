#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int k=1;k<=T;k++) {
		char s[1002];
		string s1;
		cin>>s;
		s1 += s[0];
		for(int i=1;i<strlen(s);i++) {
			if(s[i]>=s1[0]) {
				s1 = s[i] + s1;
			}
			else {
				s1 = s1 + s[i];
			}
		}
		cout<<"Case #"<<k<<": "<<s1<<endl;
	}
	return 0;
}
