#include<bits/stdc++.h>
#define ll long long
using namespace std;



void func() {
	string s;
	cin>>s;
	ll l = s.length(),i;
	ll a[26];
	for(i=0;i<26;i++) {
		a[i]=0;
	}
	for(i=0;i<l;i++) {
		a[(s[i]-'A')]++;
	}
	ll b[10]; for(i=0;i<10;i++) b[i]=0;
	//0 ZERO
	while(a['Z'-'A'] >0) {
		b[0]++;
		a['Z'-'A']--;
		a['E'-'A']--;
		a['R'-'A']--;
		a['O'-'A']--;
	}
	
	// 2 TWO
	while(a['W'-'A'] > 0) {
		b[2]++;
		a['T'-'A']--;
		a['W'-'A']--;
		a['O'-'A']--;
	}
	
	// 6 SIX
	while(a['X'-'A'] > 0) {
		b[6]++;
		a['S'-'A']--;
		a['I'-'A']--;
		a['X'-'A']--;
	}
	
	// 7 SEVEN
	while(a['S'-'A'] > 0) {
		b[7]++;
		a['S'-'A']--;
		a['E'-'A']-=2;
		a['V'-'A']--;
		a['N'-'A']--;
	}
	
	// 8 EIGHT
	while(a['G'-'A'] > 0) {
		b[8]++;
		a['E'-'A']--;
		a['I'-'A']--;
		a['G'-'A']--;
		a['H'-'A']--;
		a['T'-'A']--;
	}
	
	// 5 FIVE
	while(a['V'-'A'] > 0) {
		b[5]++;
		a['F'-'A']--;
		a['I'-'A']--;
		a['V'-'A']--;
		a['E'-'A']--;
	}
	
	// 3 THREE
	while(a['T'-'A'] > 0) {
		b[3]++;
		a['T'-'A']--;
		a['H'-'A']--;
		a['R'-'A']--;
		a['E'-'A']-=2;
	}
	
	// 4 FOUR
	while(a['U'-'A'] > 0) {
		b[4]++;
		a['F'-'A']--;
		a['O'-'A']--;
		a['U'-'A']--;
		a['R'-'A']--;
	}
	
	// 1 ONE
	while(a['O'-'A'] > 0) {
		b[1]++;
		a['O'-'A']--;
		a['N'-'A']--;
		a['E'-'A']--;
	}
	
	// 9 NINE
	while(a['N'-'A'] > 0) {
		b[9]++;
		a['N'-'A']-=2;
	}
	cout<<" ";
	for(i=0;i<10;i++) {
		while(b[i] > 0) {
			cout<<i;
			b[i]--;
		}
	}
}

int main() {
	ll n,i;
	cin>>n;
	for(i=1;i<=n;i++) {
		cout<<"Case #"<<i<<":";
		func();
		cout<<endl;
	}
}
