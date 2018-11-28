#include<iostream>
using namespace std;
int main()
{
	freopen("output.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	int t,l;
	cin>>t;
	l=t;
	while(t--)
	{
		long long a[10]={0},n,flag=1,c=0,k,d,x=0,i;
		cin>>n;
		if(n==0)
		flag=0;
		else
		{
			for( i=1;;i++)
			{
				k=n*i;
				while(k!=0)
				{
					d=k%10;
					k=k/10;
					if(a[d]==0)
					{
						a[d]=1;
						c++;
						if(c==10)
						{
							x=1;
							break;
						}	
					}		
				}
				if(x==1)
				break;
			}
		}
		if(flag==0)
		cout<<"Case #"<<l-t<<":"<<" "<<"INSOMNIA\n";
		else
		cout<<"Case #"<<l-t<<":"<<" "<<(n*i)<<endl;
	}
	return 0;
}
