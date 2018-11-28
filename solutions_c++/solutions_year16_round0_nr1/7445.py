#include<iostream>
using namespace std;

int main()
{
	long long int t,n,d,f=0;
	//int a[10]={0,1,2,3,4,5,6,7,8,9};
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		cin>>n;
		if(n==0)
			 cout<<"Case #"<<i+1<<": "<<"Insomnia"<<endl;

if(n!=0)			
{		f=0;
		long long int a[10]={0,1,2,3,4,5,6,7,8,9};	
		long long int x;
		long long int y=n;

	      while(y<=1000*n)
	      {	x=y;
		while(x>0)
		{
			d=x%10;

			for(int k=0;k<10;k++)
				if(a[k]==d)
				{	
					a[k]=-1;
				}	
							
			f=0;
	
			x=x/10;
		}
		
		 for(int k=0;k<10;k++)
                        {
                                if(a[k]!=-1)
                                         f=1;
                        }

                        if(f==0)
                        {       cout<<"Case #"<<i+1<<": "<<y<<endl;
                               
                              y=20000*n;  
                        }

		else y=y+n;
		

			
	      }   	
	
	if(f==1)	
         	cout<<"Case #"<<i+1<<": "<<"Insomnia"<<endl;	

	
}	}	
return 0;
}

