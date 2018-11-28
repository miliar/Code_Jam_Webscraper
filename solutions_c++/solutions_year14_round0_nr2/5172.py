#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<utility>
#define P 1e-9

using namespace std;

int main()

{
  	  
  int t,count=1;
  cin>>t;
  double c,f,x;
  while(count++<=t)
    {
      cin>>c>>f>>x;
      if((x-c)>P)
	{
	  //int n=ceil((x-c)/c - (2.0/f));
	  double s,min=x/2.0,sum=0.0;
      int i;
      for(i=0; ;i++)
	{
	  sum+=c/(2+i*f);
          s=x/(2+(i+1)*f)+sum;
	  if(min-s>P)
	    {
	      min=s;
	    }
	  else
	    {
	      break;
	    }
	}
      cout<<"Case #"<<count-1<<": ";
      printf("%.7lf\n",min);
	}
      else
	{
	  cout<<"Case #"<<count-1<<": ";
	  printf("%.7lf\n",x/2.0);
	}
    }
  return 0;
}
	
