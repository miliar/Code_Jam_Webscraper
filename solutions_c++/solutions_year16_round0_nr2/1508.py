#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;
#define pb push_back
#define ft first
#define se second
#define mp make_pair

int main(){
	int t;
	cin >> t;
	for(int no = 1; no <= t; no++){
		string s;
		cin >> s;
		int count = 0;
		s.push_back('+');
		int len = s.length();
		for(int i = 0; i < len - 1; i++) if(s[i] != s[i + 1]) count++;
		cout << "Case #" << no << ": " << count << endl;
	}
}