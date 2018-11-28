#include <iostream>
using namespace std;
int main()
{
	long int q,t,num,b,c,temp,check;
	static int a[10];
	cin>>t;
	q=1;
	do{
		cin>>num;
		if(num==0)
		{cout<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;
		}
		else{
			for(int k=0;k<=9;k++)
			{a[k]=0;
			}
		
		for(int i=1;i<=100000;i++)
		{
			
			b=i*num;
			
			c=b;
			while(c>0)
			{temp=c%10;
			a[temp]=1;
				
			c=c/10;	
			
			
			}
			check=0;
			for(int j=0;j<=9;j++)
			{
				if(a[j]==0)
				{
				check=1;	
				}
			}
			if(check==0)
			{cout<<"Case #"<<q<<": "<<b<<endl;
			break;
			}
			
			
		}
	}
		
		
		
		
	q++;}while(q<=t);
	
	return 0;
}