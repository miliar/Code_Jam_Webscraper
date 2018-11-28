#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *fout = freopen("output3.txt", "w", stdout);
	long long int t,n,k,f,i,j,x,z=1;
	cin>>t;
	while(t--)
	{
		int a[10]={0};
		cin>>n;
		cout<<"Case #"<<z++<<": ";
		k=n;
		if(n==0)
		cout<<"INSOMNIA\n";
		else
		{
		while(k>0)
		{
			a[k%10]=1;
			k=k/10;
		}f=0;
		for(i=0;i<10;i++)
		{
			if(a[i]==0)
			{
			f=1;
			break;	
			}
		}
		if(f==0)
		cout<<"0\n";
		else 
		{
			for(i=2;;i++)
			{
				f=0;
				k=i*n;
				x=k;
			while(k>0)
		    {
			a[k%10]=1;
			k=k/10;
		    }
		    for(j=0;j<10;j++)
		    {
			if(a[j]==0)
			{
				f=1;
				break;
		    }}
			if(f==0) 
			{
			cout<<x<<endl;
			break;	
			}
			}}
		}
	}
	return 0;
}
