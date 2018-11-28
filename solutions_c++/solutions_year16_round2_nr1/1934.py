#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int t;
	cin>>t;
	string s;
	for(int tc = 1; tc <= t; tc++) {
		cin>>s;
		vector<int> v(30,0);
		vector<int> sol;
		for(int i = 0; i < s.size(); i++){
			v[s[i] - 'A']++;
		}
		if(v['Z' - 'A'] > 0){
			for(int i = 0; i < v['Z' - 'A']; i++)
				sol.push_back(0);
			v['E' - 'A'] -= v['Z' - 'A'];
			v['R' - 'A'] -= v['Z' - 'A'];
			v['O' - 'A'] -= v['Z' - 'A'];
			v['Z' - 'A'] = 0;
		}
		if(v['W' - 'A'] > 0){
			for(int i = 0; i < v['W' - 'A']; i++)
				sol.push_back(2);
			v['T' - 'A'] -= v['W' - 'A'];
			v['O' - 'A'] -= v['W' - 'A'];
			v['W' - 'A'] = 0;
		}
		if(v['X' - 'A'] > 0){
			for(int i = 0; i < v['X' - 'A']; i++)
				sol.push_back(6);
			v['S' - 'A'] -= v['X' - 'A'];
			v['I' - 'A'] -= v['X' - 'A'];
			v['X' - 'A'] = 0;
		}
		if(v['G' - 'A'] > 0){
			for(int i = 0; i < v['G' - 'A']; i++)
				sol.push_back(8);
			v['E' - 'A'] -= v['G' - 'A'];
			v['I' - 'A'] -= v['G' - 'A'];
			v['H' - 'A'] -= v['G' - 'A'];
			v['T' - 'A'] -= v['G' - 'A'];
			v['G' - 'A'] = 0;
		}
		if(v['H' - 'A'] > 0){
			for(int i = 0; i < v['H' - 'A']; i++)
				sol.push_back(3);
			v['T' - 'A'] -= v['H' - 'A'];
			v['R' - 'A'] -= v['H' - 'A'];
			v['E' - 'A'] -= (2 * v['H' - 'A']);
			v['H' - 'A'] = 0;
		}
		if(v['S' - 'A'] > 0){
			for(int i = 0; i < v['S' - 'A']; i++)
				sol.push_back(7);
			v['N' - 'A'] -= v['S' - 'A'];
			v['V' - 'A'] -= v['S' - 'A'];
			v['E' - 'A'] -= (2 * v['S' - 'A']);
			v['S' - 'A'] = 0;
		}
		if(v['V' - 'A'] > 0){
			for(int i = 0; i < v['V' - 'A']; i++)
				sol.push_back(5);
			v['F' - 'A'] -= v['V' - 'A'];
			v['I' - 'A'] -= v['V' - 'A'];
			v['E' - 'A'] -= v['V' - 'A'];
			v['V' - 'A'] = 0;
		}
		if(v['R' - 'A'] > 0){
			for(int i = 0; i < v['R' - 'A']; i++)
				sol.push_back(4);
			v['F' - 'A'] -= v['R' - 'A'];
			v['O' - 'A'] -= v['R' - 'A'];
			v['U' - 'A'] -= v['R' - 'A'];
			v['R' - 'A'] = 0;
		}
		if(v['O' - 'A'] > 0){
			for(int i = 0; i < v['O' - 'A']; i++)
				sol.push_back(1);
			v['N' - 'A'] -= v['O' - 'A'];
			v['E' - 'A'] -= v['O' - 'A'];
			v['O' - 'A'] = 0;
		}
		if(v['E' - 'A'] > 0){
			for(int i = 0; i < v['E' - 'A']; i++)
				sol.push_back(9);
			v['N' - 'A'] -= (2 * v['E' - 'A']);
			v['I' - 'A'] -= v['E' - 'A'];
			v['E' - 'A'] = 0;
		}
		cout<<"Case #"<<tc<<": ";
		sort(sol.begin(),sol.end());
		for(int i = 0; i < sol.size(); i++){
			cout<<sol[i];
		}
		cout<<endl;
	} 
	return 0;
}