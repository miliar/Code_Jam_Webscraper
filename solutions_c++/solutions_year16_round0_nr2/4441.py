#include <iostream>
#include <cstring>
using namespace std;

void function(char c[], int t)
{
	int count,tot;
	int l=strlen(c);
	if(l<=1)
	{
		if(l==0)
			cout<<"Case #"<<t<<": 0"<<endl;
		else
		{
			if(c[0]=='+')
				cout<<"Case #"<<t<<": 0"<<endl;
			else if(c[0]=='-')
				cout<<"Case #"<<t<<": 1"<<endl;
		}
	}
	else
	{
		tot=0;
		count=0;
		for(int i=0;i<(l-1);i++)
		    if(c[i]=='-' && c[i+1]=='+')
			    count=count+1;
		if(c[0]=='+' && c[l-1]=='+')
			tot=2*count;
		else if(c[0]=='+' && c[l-1]=='-')
			tot=(2*count)+2;
		else if(c[0]=='-' && c[l-1]=='+')
			tot=(2*(count-1))+1;
		else if(c[0]=='-' && c[l-1]=='-')
			tot=(2*count)+1;
		cout<<"Case #"<<t<<": "<<tot<<endl;
	}		
}

int main()
{
	int t,i;
	char c[100];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>c;
		function(c,(i+1));
	}
	return 0;
}