#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main() {
	int t, i;
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("sollargeA.out");
	fin>>t;
	for (i=1;i<=t;i++) {
		string s;
		fin>>s;
		fout<<"Case #"<<i<<": ";
		list<int> a;
		a.push_back(s[0]-'A');
		int j;
		for (j=1;j<s.length();j++) {
			if (a.front()<=(s[j]-'A'))
				a.push_front(s[j]-'A');
			else 
				a.push_back(s[j]-'A');
		}
		for (list<int>::iterator it=a.begin();it!=a.end();it++) {
			fout<<char((*it)+'A');
		}
		fout<<endl;
		a.clear();
	}
	return 0;
}
