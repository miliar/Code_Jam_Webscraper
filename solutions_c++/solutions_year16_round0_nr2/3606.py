#include <bits/stdc++.h>
using namespace std;

int Plus [10000];
int Minus [10000];

int main () {
	ios_base::sync_with_stdio(0);
	int t;
	string s;
	cin >> t;
	for (int x=1; x<=t; x++) {
		cin >> s;
		for (int i=0; i<=s.size(); i++) {
			Plus[i]=0;
			Minus[i]=0;
		}
		if (s[0]=='+') Minus[0]=1;
		else Plus[0]=1;
		for (int i=1; i<s.size(); i++) {
			if (s[i]=='+') {
				Plus[i]=Plus[i-1];
				Minus[i]=Plus[i-1]+1;
			}
			else {
				Minus[i]=Minus[i-1];
				Plus[i]= Minus[i-1]+1;
			}
		}
		cout << "Case #" << x << ": " << Plus[s.size()-1] << "\n";
	}
}