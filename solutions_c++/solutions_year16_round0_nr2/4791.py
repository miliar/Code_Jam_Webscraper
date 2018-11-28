#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	long long T,N,n,t,c;
	string s;
	cin >>T;
	for(int j=0;j<T;j++) {
		cin >>s;
		c = 0;
		int sign = s[0]=='+'?1:-1;
		for(int i=1;i<s.length();i++) {
			if(s[i]!=s[i-1]) {
				c++;
				sign *= -1;
			}
		}
		if(sign == -1)	c++;
		cout<<"Case #"<<(j+1)<<": "<<c<<endl;
	}
	return 0;
}