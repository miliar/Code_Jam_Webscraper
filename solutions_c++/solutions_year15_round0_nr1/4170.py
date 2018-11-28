#include <iostream>
#include <cstdio>
using namespace std;

int main(void) {
	int t; scanf("%d\n", &t);
	for(int cc=1;cc<=t;cc++) {
		int n; cin>>n; n++;
		string s; cin>>s;
		int fr=0, op=0;
		if(s.at(0)==0) {op=1; fr++;}
		else op=s.at(0)-'0';
		for(int ii=1;ii<s.length();ii++) {
			if(op>=ii)
				op+=(s[ii]-'0');
			else {
				int pf=(ii-op);
				fr+=pf;
				op+=pf+(s[ii]-'0');
			}
		}
		printf("Case #%d: %d\n", cc, fr);
	}
}