#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;int flag=1,temp=0,flag1=0,k=0,l=1,loc=-1,n;
	unsigned long a[10];
	cin>>t;
	unsigned long out[t];
	for(int i=0;i<10;i++)
	a[i]=-1;
	for(int i=0;i<t;i++)
	{cin>>n;int alt=n;k=0;l=1;flag=1;
		if(n==0)
		{
			loc=i;
		}
		else{
		while(flag==1)
		{
			while(alt>0)
			{
				temp=alt%10;
				alt=alt/10;flag1=0;
					for(int j=0;j<k;j++)
					{
						if(temp==a[j])
						{
							flag1=1;
							break;
						}
					}
				if(flag1==0)
				{
					a[k]=temp;
					k++;
				}
			}
			if(k==10)
			{
				flag=0;
				out[i]=l*n;
			}
			else
			{
				alt=(l+1)*n;
				l++;
			}
		}
	}
	}
	for(int i=0;i<t;i++)
	{
		if(i==loc)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
		}
		else
		cout<<"Case #"<<i+1<<": "<<out[i]<<"\n";
	}
}
