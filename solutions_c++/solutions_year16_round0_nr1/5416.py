#include<bits/stdc++.h>


using namespace std;

int main()
{
	int t,n,k,sum=0,m,rem,l,f[10];
	cin>>t;
	k=1; 
	while(t--)
	{  
		//sum=0;
		for(int i=0;i<10;i++)
			f[i]=0;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<k++<<": "<<"INSOMNIA"<<endl;
		else
		{    l=n;
			   int i=1;
			  while(1)
			  {
                   // cout<<n<<" ";
			  	 m=n;
            		 while (n != 0)
	  				 {

					      rem = n % 10;
					      f[rem]++;
					      n= n / 10;
					   } 
					  sum=0; 
				   for(int j=0;j<10;j++)
				   {
				   	   if(f[j]==0)
				   	   	{sum=1;
				   	   		break;
				   	   	}
				   	  
				   }
				   if(sum==0)
				   {
				   	cout<<"Case #"<<k++<<": "<<m<<endl;
				   	  break;
				   }
				   n=(++i)*l;
				}
		}

	}
}