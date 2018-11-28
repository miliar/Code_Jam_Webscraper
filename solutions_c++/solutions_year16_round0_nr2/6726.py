#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	long long int t,x,f,i;
	cin>>t;
	
	for(x=1;x<=t;x++)
	{
		char c[300];
		scanf("%s",&c);
		f=0;
		if(c[0]=='-')
		f=1;
		for(i=1;c[i]!='\0';i++)
		{
			if((c[i]=='-')&&(c[i-1]=='+'))
			f+=2;
		}
		cout<<"Case #"<<x<<": "<<f;
		cout<<endl;
	}
}