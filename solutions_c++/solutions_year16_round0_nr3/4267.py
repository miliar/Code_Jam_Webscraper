#include<iostream>
#include<stdio.h>
#include<cstring>
#include<math.h>
using namespace std;
int n,d[9];
char c[33];
void decimaltobinary(double d)
{
	int i=1,rem,e;
	e=0;
    	do
    	{
		rem= fmod(d,2.0);
		c[e]=rem+48.0;
        	d=d/2.0;
		e++;
    	}while(d>0);
	/*for(i=n;i>=0;i--)
	{
		cout<<c[i];
	}
	cout<<"\n";*/
}
int basecheck()
{
	int i,j,k=0,flag;
	double a,b,sum,l;
	for(i=2;i<=10;i++)
	{
		flag=0;
		sum=0;
		for(j=n;j>=0;j--)
		{
			a=c[j]-48.0;
			b=a*pow(i,j);
			sum=sum+b;
		}
		for(l=2;l<=sum/2;l++)
  		{	
      			if(fmod(sum,l)==0)
      			{
				d[k]=l;
          			flag=1;
				break;
     			}
  		}
		if(flag==0)
		{
			return 1;
		}
		k++;
	}
	return 0;
}
int main()
{
	double t,z=0,a,b,i,e,f=0;
	int j,k;
	cin>>t;	
	cin>>n>>j;
	n=n-1;
	a=pow(2,n);
	b=pow(2,n+1);
	while(z<t)
	{	cout<<"Case #"<<t<<":"<<"\n";
		for(i=a+1;f<j;i=i+2)
		{
			if(a<b)
			{	
				decimaltobinary(i);
				e=basecheck();
				if(e==1)
				{
					a=a+2;
				}	
				else
				{
					for(k=n;k>=0;k--)
					{
						cout<<c[k];
					}			
					for(k=0;k<9;k++)
					{
						cout<<" "<<d[k];
					}
					f++;
					cout<<"\n";
				}
			}
			else
			{
				break;
			}
		}
		z++;
	}	
	return 0;
}	
