#include<bits/stdc++.h>
#define max 100000000
using namespace std;
int main()
{
	long long int n,t,i,j,k=0,l,m,f,z;
	cin >> t;
	cin >> n >> t;
	cout << "Case #1:" << endl;
	m=n-2;
	int a[n];
	a[0]=1;
	a[n-1]=1;
	for(i=(1<<m)-1;i>=0;i--)
	{
		long long int div[9]={1};l=0;
		for(j=0;j<m;j++)
		{
			if(i&(1<<j))
				a[j+1]=1;
			else
				a[j+1]=0;
		}
		for(l=2;l<=10;l++)
		{
			k=0;f=0;z=0;
			for(j=n-1;j>=0;j--)
			{
				k=k+a[j]*pow(l,f);
				f++;
			}
			for(j=2;j*j<k;j++)
			{
				if(k%j==0)
				{
					div[l-2]=j;
					//cout << div[l-2] << endl;
					z=1;
					break;
				}
			}
			if(z==0)
				break;
		}
		if(l==11)
		{
			for(k=0;k<n;k++)
			{
				cout << a[k];
			}
			t--;
			cout << " ";
			for(k=0;k<9;k++)
				cout << div[k] << " ";
			cout << endl;
		}
		if(t<=0)
			break;
	}
}
