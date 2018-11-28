#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>

using namespace std;

int smax;
string s;

int main(){
	int t;

	cin>>t;
	int cas = t;
	while (t--){
		cin>>smax>>s;
		int tot=0;
		int add=0;
		int must=0;
		for (int i=0; i<=smax; i++){
		    must = i;
			if (must>tot && (s[i]-'0')>0){
				add += must-tot;
				tot += must-tot;
			}
				tot += s[i]-'0';

		}
		cout<<"Case #"<<cas-t<<": "<<add<<"\n";
	}
}
