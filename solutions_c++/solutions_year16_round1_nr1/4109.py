#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.rtf","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	string s="",r="";
	cin>>s;
	
	int a=s.size();
	
	r+=s[0];
	for(int j=1;j<a;j++)
	{
		string c;
		c=s[j];
		if(r[0] > s[j])
		r+=s[j];
		
		else
		{
		r.insert(0,c);
		//cout<<r<<"\n";
		}
	}
	
	cout<<"Case "<<"#"<<i+1<<": "<<r;
	if(i+1!=t)
	cout<<"\n";
	}
	return 0;
}
