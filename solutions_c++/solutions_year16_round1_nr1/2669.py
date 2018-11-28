#include<bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		string s; cin>>s;
		int n=s.size();
		string t;
		for (int i=0; i<n; i++) {
			char ch=s[i];
			if(i==0) t+=ch;
			else if(ch>=t[0]) t=ch+t;
			else t+=ch;
		}
		cout << "Case #" << c << ": " << t << endl;
	}
	return 0;
}
