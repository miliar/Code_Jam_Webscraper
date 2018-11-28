#include <iostream>
#include <fstream>

using namespace std;

bool done(string s);
bool allneg(string s);

int main() {
	int t, i;
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("sollarge2.out");
	fin>>t;
	//cin>>t;
	for (i=1;i<=t;i++) {
		long long ans=0;
		string s;
		fin>>s;
		fout<<"Case #"<<i<<": ";
		if (s.length()==1 && s[0]=='-')
			ans = 1;
		else if (s.length()==1 && s[0]=='+')
			ans = 0;
		else {
		while (!done(s)) {
			int k;
			for (k=0;k<s.length()-1;k++) {
				if (s[k]!=s[k+1]) {
					ans++;
					break;
				}
			}
			for (int j=0;j<=k;j++) {
				s[j] = s[k+1];
			}
			if (allneg(s)) {
				ans++;
				break;
			}
		}
		}
		fout<<ans<<endl;
	}
	return 0;
}	

bool allneg(string s) {
	int i;
	for (i=0;i<s.length();i++) {
		if (s[i]=='+')
			return false;
	}
	return true;
}

bool done(string s) {
	int i;
	for (i=0;i<s.length();i++) {
		if (s[i]=='-')
			return false;
	}
	return true;
}

