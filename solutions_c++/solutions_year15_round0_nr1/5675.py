#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t=0,j=1;
	cin>>t;
	string s;
	long n=0,i;
	long sum=0,count=0;
	while(t--)
	{
		sum=0;
		cin>>n>>s;
		i=0;count=0;
		while(i<n+1)
		{
			if(sum>=i)
			{
				sum=sum+(int)s[i]-48;	
			}
			else
			{
				count=count+(i-sum);
				sum=sum+(int)s[i]-48+(i-sum);
			
			}
			i++;
		}
		cout<<"Case #"<<j<<": "<<count<<endl;
		j++;
		
	}
	return 0;
}