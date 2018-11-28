#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define ll long long
#define EPS 1e-7
using namespace std;
ll a[1000000];
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		string s,t;
		cin >> s;
		for (int i = 0; i < s.length(); ++i){
			a[s[i]]++;
		}
		while (a['Z']>0)
		{
			a['Z']--;
			t += '0'; a['E']--; a['R']--; a['O']--; 
		}
		while (a['W']>0)
		{
			a['W']--;
			t += '2'; a['T']--; a['O']--;
		}
		while (a['U']>0)
		{
			t += '4'; a['U']--; a['F']--; a['O']--; a['R']--;
		}
		while (a['X']>0)
		{
			a['X']--;
			t += '6'; a['S']--; a['I']--;
		}
		while (a['G']>0)
		{
			a['G']--;
			t += '8'; a['I']--; a['E']--; a['H']--; a['T']--;
		}
		while (a['T']&&a['H'])
		{
			t += '3'; a['T']--; a['H']--; a['E']--; a['R']--; a['E']--;
		}
		while (a['V'] && a['F'])
		{
			t += '5'; a['F']--; a['I']--; a['V']--; a['E']--;
		}
		while (a['V'] && a['S'])
		{
			t += '7'; a['S']--; a['E']--; a['V']--; a['E']--; a['N']--;
		}
		while (a['O'] && a['N'])
		{
			t += '1'; a['O']--; a['N']--; a['E']--;
		}
		while (a['N'] && a['I'])
		{
			t += '9'; a['N']--; a['I']--; a['N']--; a['E']--; 
		}
		sort(t.begin(), t.end());
		cout << "Case #" << k << ": "<<t <<  endl;
	}

	//system("pause");
}