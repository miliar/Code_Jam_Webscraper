#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,s,j=0;
	cin>>t;
	while(t--)
	{
		j++;
		cin>>s;
		char arr[s+1];
		scanf("%s",arr);
		//printf("%s\n",arr);
		int c=arr[0]-48,f=0;
		for(int i=1;i<=s;i++)
		{
			if(c>=i)
			{
				//cout<<c<<"\n";
			}
			else
			{
				f++;
				c++;
				//cout<<"f="<<f<<"\n";
			}
			c+=(arr[i]-48);
		}
		cout<<"Case #"<<j<<": "<<f<<"\n";
		
	}
	// your code goes here
	return 0;
}
