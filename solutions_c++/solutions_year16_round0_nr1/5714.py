#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int ii=1;ii<=t;ii++)
	{
		long long int n,i=1,mul,c,a[10],flag=0;
		cin >> n;
		if(n==0)
		{
			cout << "Case #"<<ii<<": INSOMNIA" << endl;
			continue;
		}
		for(int j=0;j<10;j++)
			a[j]=j;
		while(1)
		{
			mul=i*n;
			c=mul;
			while(mul>=1)
			{
				int p=mul%10;
				if(a[p]!=12)
				{
					a[p]=12;
					flag++;
				}
				if(flag==10)
					break;
				mul/=10;
			}
			if(flag==10)
					break;
			i++;
		}
		cout <<"Case #"<<ii<<": "<<c << endl;
	}
}
