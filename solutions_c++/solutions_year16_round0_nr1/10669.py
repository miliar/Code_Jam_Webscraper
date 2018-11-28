#include<bits/stdc++.h>
using namespace std;

int main()
{
  int t,n;
  cin>>t;
  int p=1;
  while(p<=t)
    {
      cin>>n;
      int a[10];
      for(int i=0;i<10;i++)
	a[i]=0;
      int f=10;
      if(n==0)
	{
	  cout<<"Case #"<<p<<": INSOMNIA"<<endl;
	//break;
	}
      else
	{
	  int k=1,l;
	  while(f>0)
	    {
	      l=k*n;
	      while(l>0)
		{
		  if(a[l%10]==0)
		    {
		      a[l%10]=1;
		      f--;
		    }
		  l=l/10;
		  if(f<=0)
		    break;
		}
	      if(f<=0)
		cout<<"Case #"<<p<<": "<<k*n<<endl;
	      k++;
	    }
	}
      p++;
    }
  return 0;
  
}
