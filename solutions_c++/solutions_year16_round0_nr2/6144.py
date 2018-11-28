#include <bits/stdc++.h>
using namespace std;

void main2(){
	string s; cin >> s;
	int res = 0;
	for (int i=0; i+1<(int)s.size(); i++) if (s[i] != s[i+1])
		res++;
	if (s[(int)s.size()-1] == '-')
		res++;
	cout << res << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
