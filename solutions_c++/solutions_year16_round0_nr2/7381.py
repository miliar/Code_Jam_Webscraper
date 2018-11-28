#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,len,c,m;
	string arr;
	cin>>t;
	for(m=1;m<=t;m++)
	{
		c=0;
		cin>>arr;
		len=arr.size();
		while(1)
		{
			i=0;
				if(arr[i]=='+')
				{
					while(arr[i]=='+')
					{
					arr[i]='-';
					i++;	
					}
					if(i==len)
					{
						cout<<"Case #"<<m<<": ";
						cout<<c<<endl;
						break;
					}
					c++;
				}
				else if(arr[i]=='-')
				{
					while(arr[i]=='-')
					{
					arr[i]='+';
					i++;	
					}
					c++;
				}
		}
	}
}
