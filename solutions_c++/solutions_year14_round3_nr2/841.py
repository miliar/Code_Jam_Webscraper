#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <vector>
#include <algorithm>

#define RPT(i, x) for (int i = 0; i < (x); i++)

using namespace std;

int check(string t) {
	bool fail = false;
	
	bool f['z'-'a'+1];
	RPT(i,'z'-'a'+1) f[i] = false;
	
	char cur = 0;
	RPT(i,t.length()) {
		if(t[i] == cur) continue;
		if(f[t[i]] == false) {f[t[i]] = true; cur = t[i]; continue;}
		fail = true;
	}
	
	
	if(fail) return 0;
	return 1;
}

int trial(vector<string> text, string rt) {
	if(text.size() == 0) return check(rt);
	
	int sub = 0;
	RPT(i, text.size()) {
		vector<string> ne;
		string put;
		
		RPT(j,text.size()) {if(j != i) ne.push_back(text[j]); else put = text[j];}
		sub += trial(ne, rt + put);
	}
	return sub % 1000000007;
}


int main() {
	int n; cin >> n;
	
	RPT(i,n)
	{
		int p; cin >> p;
		
		vector<string> text;
		RPT(j,p){string foo; cin >> foo; text.push_back(foo);}
		
		cout << "Case #" << i+1 << ": " << trial(text,"") << endl;		
		
				
	}
	
	return 0;	
}
