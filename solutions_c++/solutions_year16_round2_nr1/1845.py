#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

int t;
string s;

int main(void) {
	
	ifstream cin("input.in");
	ofstream cout("output.out");
	
	cin>>t;
	
	getline(cin,s);
	
	for (int c=1; c<=t; ++c) {
		
	   getline(cin,s);
	
		int l[30], f[10];
		
		memset(l,0,sizeof(l));
		memset(f,0,sizeof(f));
		
		for (int i=0; i<s.length(); ++i) ++l[s[i]-'A'];
		
		while ( l['Z'-'A']>0 ) {
			++f[0];
			--l['Z'-'A'];
			--l['E'-'A'];
			--l['R'-'A'];
			--l['O'-'A'];
		}
		
       while ( l['W'-'A']>0 ) {
			++f[2];
			--l['T'-'A'];
			--l['W'-'A'];
			--l['O'-'A'];
		}
		
		while ( l['X'-'A']>0 ) {
			++f[6];
			--l['S'-'A'];
			--l['I'-'A'];
			--l['X'-'A'];
		}
		
		while ( l['U'-'A']>0 ) {
			++f[4];
			--l['F'-'A'];
			--l['O'-'A'];
			--l['U'-'A'];
			--l['R'-'A'];
		}
		
		while ( l['O'-'A']>0 ) {
			++f[1];
			--l['O'-'A'];
			--l['N'-'A'];
			--l['E'-'A'];
		}
		
		
		while ( l['S'-'A']>0 ) {
			++f[7];
			--l['S'-'A'];
			--l['E'-'A'];
			--l['V'-'A'];
			--l['E'-'A'];
			--l['N'-'A'];
			
		}
		
		while ( l['R'-'A']>0 ) {
			++f[3];
			--l['T'-'A'];
			--l['H'-'A'];
			--l['R'-'A'];
			--l['E'-'A'];
			--l['E'-'A'];
		}
		
		while ( l['V'-'A']>0 ) {
			++f[5];
			--l['F'-'A'];
			--l['I'-'A'];
			--l['V'-'A'];
			--l['E'-'A'];
		}
		
		while ( l['G'-'A']>0 ) {
			++f[8];
			--l['E'-'A'];
			--l['I'-'A'];
			--l['G'-'A'];
			--l['H'-'A'];
			--l['T'-'A'];
		}
		
		while ( l['N'-'A']>0 ) {
			++f[9];
			--l['N'-'A'];
			--l['I'-'A'];
			--l['N'-'A'];
			--l['E'-'A'];
		}
		
		cout<<"Case #"<<c<<": ";
		
		for (int i=0; i<10; ++i)
		 for (int j=1; j<=f[i]; ++j) cout<<i;
		 
	   cout<<"\n";

	}
	
	return 0;
}
