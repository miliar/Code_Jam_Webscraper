#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{ long long int a,b,k,i,j,c=0,t,ways=0;
  cin>>t;
  while(t--)
  { ++c;
    ways=0;
    cin>>a>>b>>k;
    for(i=0;i<a;i++)
      { for(j=0;j<b;j++)
      	  {  if( (i&j) < k)
			  {  
			     ++ways;
		      }
      	  	 
      	  }
      }
  	cout<<"Case #"<<c<<": "<<ways<<endl;
  }

  return 0;	
}
