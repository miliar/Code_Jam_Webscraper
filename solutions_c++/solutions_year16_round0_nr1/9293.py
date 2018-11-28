#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,l,n,i,j,k,fg;
	cin>>t;
	for(l=1;l<=t;l++)
	{
		cin>>n;
		long long int a[10]={0};
		for(i=1;i<1000000;i++)
		{
			fg=0;
			j=n*i;
			while(j)
			{
				k=j%10;
				a[k]=1;
				j/=10;
			}
			for(k=0;k<10;k++)
				if(a[k]==0)
					fg=1;
			if(fg==0)
			{
				cout<<"Case #"<<l<<": "<<n*i<<endl;
				break;
			}
		}
		if(i==1000000)
			cout<<"Case #"<<l<<": INSOMNIA\n";
	}
	return 0;
}