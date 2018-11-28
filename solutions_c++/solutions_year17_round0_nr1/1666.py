#include <iostream>
#include <fstream>
#include <string>
#define DN 1000
using namespace std;

int T,k;
string s;

int main() {
	ifstream f("a.txt");
	ofstream g("a.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		f>>s>>k;
		int r=0;
		for(int i=s.size()-1; i>=k-1; --i) if(s[i]=='-') {
			++r;
			s[i]='+';
			for(int j=1; j<k; ++j)
				if(s[i-j]=='+') s[i-j]='-';
				else s[i-j]='+';
			
		}
		int ok=1;
		for(auto i:s) if(i=='-') ok=0;
		g<<"Case #"<<t<<": ";
		if(ok) g<<r;
		else g<<"IMPOSSIBLE";
		g<<'\n';
	}
}