#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
	int t, i;
	char a[1010];
	int b[1010];
	cin>>t;
	int k = 1;
	while(t--)
	{
		int smax;
		cin>>smax;
		cin>>a;
		for(i=0;i<=strlen(a);i++)
		{
			b[i] = a[i] - 48;
		}
		int count = 0, temp = 0;
		count  = b[0];
		for(i=1;i<=strlen(a);i++)
		{
			if(i <= count )
			{
				count += b[i];
			}
			else 
			{
				count += i - count + b[i];
				temp++;
			}
		}
	cout<<"Case #"<<k<<": "<<temp<<endl;	
	k++;
	}
	return 0;
	
}	
