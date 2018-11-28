#include <bits/stdc++.h>
#define ll long long

// IDE: Code::Blocks
// Programming language: c++11
// Compiler: g++

using namespace std;

int main()
{
	// input and output files data.in and output.out
	ifstream cin("data.in");
	ofstream cout("output.out");
    int t;
    cin>>t;
    for(int i=1; i<=t; i++){
		string s;
		int k;
		cin>>s>>k;
		int cnt=0;
		for(int i=0; i<s.size()-k+1; i++){
			if(s[i]=='-'){
				cnt++;
				for(int j=0; j<k; j++){
					s[i+j]=(s[i+j]=='+'?'-':'+');
				}
			}
		}
		bool lg=true;
		for(int i=s.size()-k+1; i<s.size(); i++){
			lg=lg&(s[i]=='+');
		}

		cout<<"Case #"<<i<<": ";
		if(lg)cout<<cnt<<endl;
		else cout<<"IMPOSSIBLE "<<endl;
    }
}
