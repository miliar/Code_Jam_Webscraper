#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>

using namespace std;
#define ll long long
int main(){
ofstream ofs;
ofs.open("out.txt");

	int t;
	cin>>t;
	int a,b,k;
	ll out;
	for(int l=1;l<=t;l++){
		cin>>a>>b>>k;
		out=0;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
			if((i&j)<k)	out+=1	;

			ofs<<"Case #"<<l<<": "<<out<<endl;
		
	
		}
return 0;
}
