
#include<iostream>
using namespace std;

int main()
{
	int b=1,r,t,i,j,m,n,a[11],f,val,v;
	
	cin>>t;
	while(t--)
	{	
		for(i=0;i<10;i++)
			a[i]=0;
		
		cin>>n;
		m=n;
		cout<<"Case #"<<b<<": ";
		
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			b++;
			continue;
		}
		v=1;
		j=1;
		while(v)
		{	
			m=n*j;
			val =m;
			while(m!=0)
			{
				r=m%10;
				a[r]=1;
				m=m/10;
				//cout<<r<<"\t"<<j<<"\t"<<m<<endl;
			}
			f=0;
			for(i=0;i<10;i++)
			{
				if(a[i]==1)
				{
					f=1;
				}
				else
				{
					f=0;
					break;
				}
			}
			if(f==1)
			{
				cout<<val<<endl;
				v=0;
				break;
			}
			m = val;
			j++;
		};
		
		b++;
	}
	return 0;
}
