#include<iostream>
using namespace std;
int main()
{
	long int T,i,N[100],j,k,n,d,c,m[100];
	cin>>T;
	for(i=0; i<T; i++)
	{
		cin>>N[i];
		j=1;
		int a[10]={0,1,2,3,4,5,6,7,8,9};
		if(N[i]!=0)
			while(1)
			{
				n=N[i]*j;
				m[i]=n;
				c=0;
				while(n!=0)
				{
					d=n%10;
					for(k=0; k<10; k++)
					{
						if(a[k]==d)
							a[k]=11;
					}
					n=n/10;
				}
				for(k=0; k<10; k++)
					if(a[k]==11)
						c++;
				if(c==10)
					break;
				j++;
			}
	}
	for(i=0; i<T; i++)
	{
		cout<<"Case #"<<i+1<<": ";
		if(N[i]==0)
			cout<<"INSOMNIA\n";
		else
			cout<<m[i]<<"\n";	
	}
}
