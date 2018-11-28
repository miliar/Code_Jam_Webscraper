#include<iostream>
using namespace std;
#include<string.h>
int main()
{
	int d,p=1;
	cin>>d;
	while(d>0)
	{	
		char s[1005]={},t[1005]={};
		cin>>s;
		char top='A';
		for(int i=0;i<strlen(s);i++)
		{
			char k[1005]={};
			if(s[i]>=top)
			{
				k[0]=s[i];
				for(int j=0;j<strlen(t);j++)
					k[j+1]=t[j];
				for(int j=0;j<strlen(k);j++)
					t[j]=k[j];
				top=s[i];	 	
			}
			else
			{
				t[strlen(t)]=s[i];
				top=t[0];
			}
		}
		cout<<"Case #"<<p<<": ";
		for(int i=0;i<strlen(t);i++)
			cout<<t[i];

			cout<<"\n";
		p++;
		d--;		
	}

	return 0;
}