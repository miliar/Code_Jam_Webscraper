#include<iostream>
using namespace std;

int main()
{
	int t,k,a[10]={1,1,1,1,1,1,1,1,1,1},flag=0,j=2,i=1;
	long long int n,tmp;
	cin>>t;
	for(i=1,k=1;i<=t;i++)
	{
		cin>>tmp;
		n=tmp;	
		if(tmp!=0)
		{
			while(flag!=10) 
			{
				while(n!=0)
				{
					if(a[n%10]==k)
					{
						a[n%10]++;
						flag++;	
					}
					n=n/10;
				}			
				n=tmp*j;
				j++;	
			}
			flag=0;
			cout<<"Case #"<<i<<": "<<n-tmp<<endl;
			j=2;
			k++;
		}
		else cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	}
	return 0;
}
