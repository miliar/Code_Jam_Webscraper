#include<iostream>
#include<string>
#include<fstream>
#define ll long long
using namespace std;
int main()
{	
	ofstream myfile;	
	myfile.open("Asmall.out");
	ll t,s,sp,spp;
	string st;
	cin>>t;
	for(ll i=1;i<=t;i++){
		sp=0;spp=0;
		cin>>s;
		ll p[s+1];
		cin>>st;
		for(ll j=0;j<s+1;j++){		
		p[j]=st[j]-'0';
		}
		for(ll j=0;j<s+1;j++){
		if(p[j]==0 && spp<j+1){
		sp++;
		spp++;
		}
		else 
		spp=spp+p[j];
		}
		myfile<<"Case #"<<i<<": "<<sp<<endl;
	}
	myfile.close();
	return 0;
}
