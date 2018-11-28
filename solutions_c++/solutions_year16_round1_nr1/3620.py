#include <bits/stdc++.h>
using namespace std;
int t;
string p;
int main(){
	cin >> t;for(int y = 1; y<=t;y++){
		cin >> p;
		char k = p[0];
		string o = "";
		o+=p[0];
		for(int i = 1;i<p.size();i++) if(p[i]<o[0]) o+=p[i]; else o = p[i]+o;
		cout << "Case #" << y << ": " << o << endl;
	}
}