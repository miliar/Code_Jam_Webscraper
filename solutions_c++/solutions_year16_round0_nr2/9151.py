#include<iostream>
#include<cmath>
#include<algorithm>
#define L 1000000007

using namespace std;
//ifstream cin("test.in");
//ofstream cout("test.out");

int n, m, h, k, r, x, T, t, f, z, i, j;
string s, v;


string Flip(int k, string s){
	int i, j;
	string c, v, x;
	c=v=x="";
	for(i=k+1; i<s.length();++i) c+=s[i];
	for(i=0; i<=k; ++i) x=s[i]+x;
	//	cout<<"x: "<<x<<"\n";
	for(i=0; i<x.length(); ++i)
		if(x[i]=='-') x[i]='+';
			else x[i]='-';
	//	cout<<"x: "<<x<<"\n";
	//	cout<<"c: "<<c<<"\n";
	v=x+c;
	return v;
}


int main(){
	cin>>T; 
	for(t=0; t<T; ++t){
		cin>>s;
		r=0; 
		i=0;
		while(i<s.length()){
			while(s[i]==s[i+1] && i<s.length()-1) ++i;
			
			if(!(i==s.length()-1 && s[i]=='+')){
				s=Flip(i, s); ++r;
			}
			++i;
		}
		if(s[s.length()-1]=='-') ++r;
		cout<<"Case #"<<t+1<<": "<<r<<"\n";		
	}
	
	return 0;
}
