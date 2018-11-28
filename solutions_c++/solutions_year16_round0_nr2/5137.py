#include <bits/stdc++.h>
using namespace std;
#define ll long long

ifstream inf("test.txt");
ofstream of("out.txt");

int main(){
	int t;
	int cs=1;
	inf>>t;
	while(t--){
		char s[200];
		inf>>s;
		int n = strlen(s);
		int i=1;
		ll int c=0;
		while(i<n){
			while(i<n && s[i]==s[0]) i++;
			if (i==n) break;
			else{
				c++;
				s[0]=s[0]=='+'?'-':'+';
			}
		}
		of << "Case #" << cs++ << ": ";
		if (s[0]=='-') c++;
		of << c << endl;
	}
	return 0;
}

