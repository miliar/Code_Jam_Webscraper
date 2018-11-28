#include<bits/stdc++.h>
#include<iostream>


using namespace std;
long long int t,n,x,y,p,r,q,k,s;

int main()
{FILE *fout = freopen("output.txt", "w", stdout);
	int f=0;
	cin>>t;int i=1;k=1;
	while(t--)
	{
		int a[10]={0};
	f=0;
	
	cin>>n; 
	x=n;
	if(n==0)
	{
		cout<<"Case #"<<k<<": INSOMNIA"<<endl;;
	}
	else
	{
	p=1;f=0;
	i=1;
		
	
	while(f!=1)
	{
		p=x*i;
		i++;
		//cout<<"\n p="<<p;
		q=p;
	
		
		while(p>0)
		{
			r=p%10;
			a[r]=1;
			p=p/10;
			s=0;
			for(int j=0;j<10;j++)
			{
				//cout<<"\n sum="<<s<<"  a="<<a[j];
			s=s+a[j];
			if(s==10)
			f=1;
			else 
			f=0;	
			}
			
			
			
		}
		
		
		
	}
	cout<<"Case #"<<k<<": "<<q<<endl;
}
	k++;
	
	
	
		
	}
	
	return 0;
}
