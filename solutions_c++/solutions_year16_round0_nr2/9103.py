#include <iostream>
using namespace std;


int main() 
{

	int t;
	cin>>t;
	char s[101];
	int l;
	int flag=0;
	int count;
	int in=1;
	while(in<=t)
	{
		count=0;
		flag=0;
		cin>>s;
		l=0;
		while(s[l]!='\0')
			l++;
		for(int i=l-1;i>=0;i--)
		{
			if(s[i]=='-'&& flag==0)
			{
				flag=1;
				count++;
			}
			else if(s[i]=='+'&& flag==1)
			{
				flag=0;
				count++;
			}
			
		}
	
		cout<<"Case #"<<in<<": "<<count<<endl;;
	
		in++;
			
	}
	
	return 0;
}
