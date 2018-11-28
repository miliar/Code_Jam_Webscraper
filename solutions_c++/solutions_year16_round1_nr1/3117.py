#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large(1).in","r",stdin);
	freopen("output.txt","w",stdout);
	int m;
	cin>>m;
	for(int t=1;t<=m;t++)
	{
string s="",s1="";
cin>>s;
for(int i=0;i<s.length();i++)
{
	char b=s.at(i);
	if(s1.length()==0)
		s1=s1+b;
	else
	{
		if((int)b>=s1.at(0))
			s1=b+s1;
		else
			s1=s1+b;
	}
	}
	cout<<"Case #"<<t<<":"<<" "<<s1<<"\n";
}

}
