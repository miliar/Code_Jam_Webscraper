#include <bits/stdc++.h>
using namespace std;

#define pp output << " 3 2 5 2 7 2 9 2 11" << endl

bool check(string s){
	int cn = 0;
	for(int i=0;i<s.length();i++){
		if(s[i]=='1') cn++;
		
	}
	return cn%2 ? 0 : 1;
}

map <string,bool> M;

int main(){
	string str = "11000000000000000000000000000011";
	string m = str, n = str;
	ofstream output;
	output.open("out.txt");
	output << "Case #1:" << endl;
	M[str]=1;
	output << str; pp;
	int cc = 1, c2 = 1;
	for(int k=2;k<str.length()-3;k++){
		string z = str;
		z[k]='1'; z[k+1]='1';
		if(check(z) && !M[z]){
			cc++;
			M[z]=1;
			output << z; pp;
			for(int u=k+2;u<str.length()-3;u++){
				string l = z;
				l[u]='1'; l[u+1]='1';
				if(check(l) && !M[l]){
					cc++;
					M[l]=1;
				
					output << l; pp;
				}
			}
		}
	}
	for(int k=2;k<str.length()-3;k++){
		string z=str;
		z[k]='1';
		z[k+1]='1';
		for(int u=k+2;u<str.length()-3;u++){
			string l =z;
			l[u]='1';
			l[u+1]='1';
			for(int j=u+2;j<str.length()-3;j++){
				string r=l;
				r[j]='1';
				r[j+1]='1';
				if(check(r) && !M[r]){
					cc++;
					M[r]=1;
				
					output << r; pp;
					if(cc==500) goto hell;
				}
			}
		}
	}
	hell:
	cout << cc << endl;
	return 0;
}
