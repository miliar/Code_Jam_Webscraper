#include <iostream>
using namespace std;

int main()
{
	int i,n,t,j,k,m,x,count;
	bool a[10];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		for(j=0;j<10;j++)
			a[j]=false;
		count=0;
		k=1;
		while(n!=0&&count!=10)
		{
			m=n*k;
			k++;
			while(m>0)
			{
				x=m%10;
				for(j=0;j<10;j++)
					if(x==j){a[j]=true;}
				m=m/10;
			}
			count=0;
			for(j=0;j<10;j++)
				if(a[j]){count++;}
		}
		if(n==0){cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";}
		else{cout<<"Case #"<<i+1<<": "<<(n*(k-1))<<"\n";}
	}
	return 0;
}