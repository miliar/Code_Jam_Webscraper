#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("abc2.in","r",stdin);
	freopen("outq2l.txt","w",stdout);
	int t,i=1,j,k,c=0,m;
	string s;
	cin>>t;
	while(i<=t)
	{
		cin>>s;
		k=s.find_first_of("+");
		j=s.find_last_of("-");
	
		while(k<j && k!=-1 && j!=-1){
			c++;
		for(m=0;m<=j;m++)
		{
			if(s[m]=='+')
			s[m]='-';
			
			else
			s[m]='+';	
		}
		k=s.find_first_of("+");
		j=s.find_last_of("-");
	}
	if(k==-1)
	cout<<"Case #"<<i<<": "<<1<<endl;
	
	else if(j==-1)
	cout<<"Case #"<<i<<": "<<0<<endl;
	else
		cout<<"Case #"<<i<<": "<<c+1<<endl;
		c=0;
		i++;
	}	
}
