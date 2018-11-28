#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,n,i,j,k,l,f,p=1;
	long long int a[10]={0};
	cin >> t;
	while(t--)
	{
		j=1;
		long long int a[10]={0};
		cin >> n;
		if(n==0)
		{
			cout << "Case #" << p << ": " <<"INSOMNIA" << endl;
			p++;
			continue;
		}
		while(1)
		{
			k=n*j;
			f=0;
			while(k!=0)
			{
				l=k%10;
				a[l]++;
				k=k/10;
			}
			for(i=0;i<10;i++)
			{
				if(a[i]==0)
				{
					f=0;
					break;
				}
				else
					f=1;
			}
			if(f==1)
			{
				cout << "Case #" << p << ": " << n*j << endl;
				break;
			}
			j++;
		}
		p++;
	}
}
