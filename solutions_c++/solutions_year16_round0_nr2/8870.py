#include<iostream>
using namespace std;
int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("B-large3.out","w",stdout);
	
	long long t,p,c,i,q;
	string s;
 	cin>>t;
 	for(q=0;q<t;q++)
 	{
 		long long int c=0;
 		cin>>s;
 		p=s.length();
 		for(i=0;i<p-1;i++)
 		{
 			if(s[i]!=s[i+1])
 			c++;
 		}
 		if(s[p-1]=='+')
 		cout<<"Case #"<<q+1<<": "<<c<<endl;
 		else
 		cout<<"Case #"<<q+1<<": "<<c+1<<endl;
 	}




}

