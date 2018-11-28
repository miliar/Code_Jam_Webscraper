#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long int t,c,d,f,i,m,l;
	char s[1000];
	cin>>t;
	l=1;
	while(l<=t)
	{
		cin>>m;
		cin>>s;
		c=s[0]-48;
		d=0;f=0;
		for(i=1;i<strlen(s);i++)
		{
			if(s[i]-48!=0)
			{
				if(c>=i)
				{
					c=c+s[i]-48;
				}
				else
				{
					d=i-c;
					f=f+d;
					c=c+d+s[i]-48;
				}
			}
		}
		cout<<"Case #"<<l<<":"<<f<<endl;
		l++;
	}
	return 0; 
}
