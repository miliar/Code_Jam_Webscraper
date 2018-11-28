#include<iostream>

using namespace std;

int T, k, n;
string s;
char l;

int main(){
	cin>>T;
	for(int t=1; t<=T; t++) {
		cin>>s;
		l = s[0];
		n = s.size();
		k = 0;
		for(int i=1; i<n; i++)
			if(l!=s[i]) {
				k++;
				l = s[i];
			}
		if(l=='-') k++;
		cout<<"Case #"<<t<<": "<<k<<endl;
	}
}