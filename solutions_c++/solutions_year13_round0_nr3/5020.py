#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;


int pali(int n);


int main()
{
	int T;
	freopen("C-small-attempt0.in","r",stdin);
		freopen("output8.in","w",stdout);
	cin>>T;
	
	int wh=T;
	
	while(T--)
	{
		
		
		int a,b,i,count=0;
		
		
		cin>>a>>b;
		
		for(i=a;i<=b;i++)
		{
			int l;
			l=pali(i);
		//	cout<<"l is "<<l<<endl;
			
			//if(l==1)
			//cout<<i<<" is palindrome"<<endl;
			
			double z=sqrt(i);
			//cout<<z<<endl;
			int k=z;
			if(k==z)
			{
			//	cout<<"entered "<<endl;
				int m=pali(k);
			//	cout<<k<<" is palindrome"<<endl;
				
				if(l==1&&m==1)
				count++;			
			}
		}
		cout<<"Case #"<<wh-T<<": "<<count<<endl;
	}
}
	
	
	
int pali(int no)
{
	int no2=no,no3=0,rem;
	
	while(no>0)
	{
		rem=no%10;
		no3=no3*10+rem;
		no=no/10;
	}
	
	if(no2==no3)
	return 1;
	else
	return 0;
}
