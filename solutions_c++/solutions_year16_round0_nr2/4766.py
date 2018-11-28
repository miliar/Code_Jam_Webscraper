#include<iostream>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
int main(){
	fstream i;
	i.open("gcjk.txt",ios::in|ios::out|ios::app);
	fstream o;
	o.open("aou.txt",ios::in|ios::out|ios::trunc);
	lli whichcase=0;
	lli t;
	i>>t;
	cout<<t<<endl;
	while(t--){
			string s;
			i>>s;
			lli l=s.size(),count=0,ic,j;
			if(l==1){
				if(s[0]=='+')
					o<<"Case #"<<++whichcase<<": "<<0<<endl;
				else {
					o<<"Case #"<<++whichcase<<": "<<1<<endl;
				}
					continue;
			}
			
			
			for(ic=0;ic<l-1;ic++){
				if(s[ic]==s[ic+1]){
					continue;
				}
				else {
					count++;
				}
			}
			if(s[l-1]=='-') count++;
			o<<"Case #"<<++whichcase<<": "<<count<<endl;
			cout<<endl;
		}
	
	i.close();
	o.close();
}

