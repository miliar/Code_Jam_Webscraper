#include<iostream>
#include <fstream>
using namespace std;
int main()
{
	int t,c=0,i=1,d,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,k;
	long long int n,n1,tmp;
	ofstream myfile;
     myfile.open ("output.txt");
	cin>>t;
	while(t--)
	{
		d=0,c=0,f0=0,f1=0,f2=0,f3=0,f4=0,f5=0,f6=0,f7=0,f8=0,f9=0;
		cin>>n;
		n1=n;
		k=2;
		while(c!=10)
		{
			tmp=n;
			while(tmp>0)
			{
				d=tmp%10;
				if(d==0 && f0==0)
				{
					c++;
					f0=1;	
				}
				if(d==1 && f1==0)
				{
					c++;
					f1=1;	
				}
				if(d==2 && f2==0)
				{
					c++;
					f2=1;	
				}
				if(d==3 && f3==0)
				{
					c++;
					f3=1;	
				}
				if(d==4 && f4==0)
				{
					c++;
					f4=1;	
				}
				if(d==5 && f5==0)
				{
					c++;
					f5=1;	
				}
				if(d==6 && f6==0)
				{
					c++;
					f6=1;	
				}
				if(d==7 && f7==0)
				{
					c++;
					f7=1;	
				}
				if(d==8 && f8==0)
				{
					c++;
					f8=1;	
				}
				if(d==9 && f9==0)
				{
					c++;
					f9=1;	
				}
				tmp=tmp/10;
			}
			if(n==0)
			{
				myfile<<"Case #"<<i<<": "<<"INSOMNIA\n";
				i++;
				break;
			}
			n=k*n1;
			k=k+1;
		}
		if(n!=0)
		{
			myfile<<"Case #"<<i<<": "<<n-n1<<endl;
			i++;
		}
	}
	myfile.close();
	return 0;
}
