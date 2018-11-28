#include "bits/stdc++.h"
using namespace std;
string f(string n){
	string out="";
	out+=n[0];
	for(int i=1;i<n.length();i++)
	{
		if(out[0]<=n[i])
			out=n[i]+out;
		else
			out=out+n[i];

	}
	return out;
}
int main(int argc, char const *argv[])
{
	int t;
	string n;
	cin>>t;
	for (int i = 1; i <=t; ++i)
	{
		cin>>n;
		cout<<"Case #"<<i<<": "<<f(n)<<endl;
	}
	return 0;
}