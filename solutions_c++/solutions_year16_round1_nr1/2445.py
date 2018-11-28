#include <bits/stdc++.h>

using namespace std;

int T;
string s;

string a,b,c;
int main() {
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> s;
		a=b=c="";
		for (int i=0;i<s.size();i++) {
			b=c=a;
			b.insert(b.begin(),s[i]);
			c.push_back(s[i]);
			a=max(b,c);
		}

		printf("Case #%d: %s\n",cas,a.c_str());
	}
}
