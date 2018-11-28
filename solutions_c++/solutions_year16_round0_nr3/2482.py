#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<math.h>

using namespace std;

int main()
{
  unsigned long long int t, n ,j, divisors[9], *number, temp, power, change=1;
  bool flag, found, bin=0;

  cin>>t;
  for(int i=1; i<=t; i++)
    {
      cin>>n;
      cin>>j;
      cout<<"Case #"<<i<<":"<<endl;
      number = new unsigned long long int[n];
      number[0] = 1;
      number[n-1] = 1;
      for(int k=1; k<n-1; k++)
	number[k] = 0;
      
      for(int k=0; k<j; k++)
	{
	  found=0;
	  while(found==0)
	    {
	      for(int l=0; l<9; l++)
		divisors[l]=0;
	      for(int l=2; l<=10; l++)
		{
		  temp=0;
		  power=0;
		  flag=0;
		  
		  for(int m=n-1; m>=0; m--)
		    {
		    temp+=number[m] * pow(l, power);
		    power++;
		    }
		  
		  for(int m=2; m<=temp/2; ++m)
		    {
		      if(temp%m==0)
			{
			  flag=1;
			  found=1;
			  divisors[l-2] = m;
			  break;
			}
		    }
		  if(flag==0)
		    {
		      found=0;
		      break;
		    }
		}
	      if(found==1)
		{
		  for(int k=0; k<n; k++)
		    cout<<number[k];
		  cout<<" ";
		  for(int l=0; l<9; l++)
		    cout<<divisors[l]<<" ";
		  cout<<endl;
		}
	      /*if(change == n-1)
		{
		  bin=1;
		  change = 1;
		}
	      if(bin == 0)
		{
		  if(number[change] == 0)
		    number[change] = 1;
		  else if(number[change] == 1)
		    number[change] = 0;
		  change++;
		}
	      else
		{
		  number[change++] = 0;
		  number[change-1] = 1;
		  if(change == n-1)
		    bin=0;
		    }
	      */
	      for(int h=n-2; h>0; h--)
		{
		  if(number[h] == 0)
		    {
		      number[h] = 1;
		      break;
		    }
		  else if(number[h] == 1)
		    {
		      number[h] = 0;
		    }
		}
	    }
	}
    }
  
  return 0;
}
