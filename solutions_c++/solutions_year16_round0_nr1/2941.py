#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
  long int t, n, digit, number, j;
  bool flag, seen[10];
  cin>>t;
  for(int i=1; i<=t; i++)
    {
      cin>>n;
      j=1;
      flag=0;
      
      while(flag==0)
	{
	  
	  if(n==0)
	    {
	      break;
	    }
	  
	  number=n * j;
	  j++;
	  
	  while (number > 0)
	    {
	      digit = number % 10;
	      seen[digit] = 1;
	      number /= 10;
	    }
	  
	  for(int k=0; k<10; k++)
	    {
	      if(seen[k] == 0)
		{
		  flag = 0;
		  break;
		}
	      else
		flag = 1;
	    }
	}

      if(flag==0)
	cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
      else
	cout<<"Case #"<<i<<": "<<n*(j-1)<<endl;
      
      for(int k=0; k<10; k++)
	{
	  seen[k] = 0;
	}
    }

  return 0;
}
