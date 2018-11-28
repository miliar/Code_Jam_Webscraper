#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t;
	cin >>t;
	long long n;
	string s;
	
	for(int i=1;i<=t;i++)
	{
		cin >>s;
		n=0;
		for(int j=s.length()-1;j>=0;j--)
		{
			
			if(s[j]=='-')
			{
				n++;
				for(int k=0;k<j;k++)
				{
					if(s[k]=='-')
						s[k]='+';
					else
						s[k]='-';
				}
			}
			if(j==0)
			{
				cout<<"Case #"<<i<<": "<<n<<endl;
				break;
			}
		}
		
				
					
					
		
	}
}
