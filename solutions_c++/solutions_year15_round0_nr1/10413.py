#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t, i,casen=1;
	char a[1001];
	int b[1001];
	cin>>t;
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
	cout<<"Case #"<<casen<<": "<<temp<<endl;
	casen++;
	}
	return 0;

}
