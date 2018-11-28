#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	for (int k=1;k<=t;k++){
		string s; int ans=0;
		cin >> s;
		string s2= "";
		for (int i=0;i<s.length();i++){
			s2+='+';
		}
		while (s != s2){
		for (int i=s.length()-1; i>=0; i--){
			if (s[i] == '-') {
				ans=ans+1;
				for (int i1=i;i1>=0;i1--){
					if (s[i1]=='-') s[i1]='+';
					else { s[i1]='-';}
				}
			}	
		}
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}
