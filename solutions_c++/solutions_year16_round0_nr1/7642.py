#include<bits/stdc++.h>
using namespace std;

long long int counts=1,n,t;
void  check (int b)
{	
	int x[11]={0,0,0,0,0,0,0,0,0,0,0};
	int a,c=0;
	int flag=1;
	int i=0;
	
	while(flag==1 && i<1000000)
	{
		int m=1;
		++i;
		c=b*i;
		a=c;
		//cout<<"      m"<<b<<"     m";
		while(a>0)
		{
			int p=a%10;
			x[p]=1;
			a=a/10;

		}
		
		//cout<<"2"<<"   "<<i;
			int j=0;
			
			while(j<=9)
			{
				m=x[j]*m;
				//cout<<m<<" "<<i;
				j++;

			}
			//cout<<"3";
			if(m==1)
					{
						flag=0;
						cout<<"Case #"<<counts<<": "<<c<<"\n";
					}
		

	}
	if(i<=1000000 && flag==1)
	cout<<"Case #"<<counts<<": "<<"INSOMNIA"<<"\n";

}


int main()
{ 
    freopen("0.in","r",stdin);
    freopen("op.txt","w",stdout);

//int x[10];
cin>>t;
while(t--)
{
	cin>>n;
	
		check(n);
		counts++;
		

}
}