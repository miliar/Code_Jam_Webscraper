#include<iostream>
#include<bits/stdc++.h>

using namespace::std;

#define lli long long int

int main(){
	lli t;
	cin>>t;	
	lli k=0;
	while(t){
		k++;
		t--;
		lli a[26]={0};
		cout<<"Case #"<<k<<": ";
		string s;
		cin>>s;
		for(lli i=0;i<s.length();i++){
			a[s[i]-'A']++;
		}
		lli d[9]={0};
		
		d[0]=a['Z'-'A'];
		
		d[2]=a['W'-'A'];

		d[4]=a['U'-'A'];
		
		d[6]=a['X'-'A'];
	
		d[8]=a['G'-'A'];

		d[1]=a['O'-'A']-d[2]-d[4] - d[0];

		d[3]=a['R'-'A']-d[0]-d[4];

		d[5]=a['F'-'A']-d[4];
			
		d[7]=a['V'-'A']-d[5];
		
		d[9]=(a['N'-'A'] - d[1]-d[7])/2 ;
		
		for(lli i=0;i<=9;i++){
			while(d[i]--){
				cout<<i;
			}
		}

		cout<<endl;
	}
	return 0;
}