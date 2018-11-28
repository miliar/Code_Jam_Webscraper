#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
#define N 100005
map<char,int> d;
vector<int> v;
void func(){
	while(d['Z'] > 0){
		d['Z']--;
		d['E']--;
		d['R']--;
		d['O']--;
		v.push_back(0);
	}
	while(d['W'] > 0){
		d['T']--;
		d['W']--;
		d['O']--;
		v.push_back(2);
	}
	while(d['U'] > 0){
		d['F']--;
		d['U']--;
		d['R']--;
		d['O']--;
		v.push_back(4);
	}
	while(d['X'] > 0){
		d['X']--;
		d['S']--;
		d['I']--;
		v.push_back(6);
	}
	while(d['G'] > 0){
		d['G']--;
		d['E']--;
		d['I']--;
		d['H']--;
		d['T']--;
		v.push_back(8);
	}
	while(d['O'] > 0){
		d['O']--;
		d['N']--;
		d['E']--;
		v.push_back(1);
	}
	while(d['S'] > 0){
		d['S']--;
		d['E']--;
		d['V']--;
		d['E']--;
		d['N']--;
		v.push_back(7);
	}
	while(d['G'] > 0){
		d['G']--;
		d['E']--;
		d['I']--;
		d['H']--;
		d['T']--;
		v.push_back(8);
	}
	while(d['V'] > 0){
		d['F']--;
		d['I']--;
		d['V']--;
		d['E']--;
		v.push_back(5);
	}
	while(d['G'] > 0){
		d['G']--;
		d['E']--;
		d['I']--;
		d['H']--;
		d['T']--;
		v.push_back(8);
	}
	while(d['T'] > 0){
		d['T']--;
		d['H']--;
		d['R']--;
		d['E']--;
		d['E']--;
		v.push_back(3);
	}
	while(d['N'] > 0){
		d['N']--;
		d['I']--;
		d['N']--;
		d['E']--;
		v.push_back(9);
	}
}

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc = 1;tc<=t;tc++){
		d.clear();
		v.clear();
		string s;
		cin>>s;
		for(int i = 0;i<s.length();i++)
		d[s[i]]++;
		func();
		sort(v.begin(),v.end());
		cout<<"Case #"<<tc<<": ";
		for(int i = 0;i<v.size();i++)
		cout<<v[i];
		cout<<endl;
	}

	return 0;
}
