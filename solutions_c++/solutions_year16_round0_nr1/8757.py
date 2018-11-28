# include<iostream>
using namespace std;
int main()
{
	long int t,n,m,i,c,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		c=0;
		bool a[10];
		int b[10]={0};
		for(i=0;i<10;i++)
			a[i]=false;
		if(n==0)
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		else
		{
			i=1;
			while(c<10)
			{
				m=n*i;
				while(m>0)
				{
					if(a[m%10]==false)
					{
						a[m%10]=true;
						b[m%10]=n*i;
						c++;
					}
					m/=10;
				}
				i++;
			}
			m=0;
			for(i=0;i<10;i++)
			{
				if(b[i]>m)
					m=b[i];
			}
			cout<<"Case #"<<j<<": "<<m<<endl;
		}
	}
	return 0;
}