#include <iostream>
#include <string>
#include <sstream>
using namespace std;
typedef unsigned long long UL;
#define MAX 1099511627776
int solve(UL p,UL q);
int main()
{
	int T,y;
	UL p,q;
	string s;
	stringstream stream;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>s;
		int pos=s.find("/");
		string s1=s.substr(0,pos);
		stream<<s1;
		stream>>p;
		stream.clear();//
		string s2=s.substr(pos+1,s.length()-pos-1);
		stream<<s2;
		stream>>q;
		stream.clear();

		cout<<"Case #"<<i<<": ";
		if((y=solve(p,q))==-1)
			cout<<"impossible"<<endl;
		else cout<<y<<endl;
	}
}
int solve(UL p,UL q)
{
	if(((p*MAX)%q)!=0)
		return -1;
	else
	{
		for(int j=1;j<40;j++)
		{
			p*=2;
			if(p>=q)
				return j;
		}
	}
}