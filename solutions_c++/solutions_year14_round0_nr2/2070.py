#include<iostream>
using  namespace std;
#include<vector>
#include<stdio.h>
int main()
 {int t,k,i,j;
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
 cin>>t;

 double x,c,f,minT;
 for(k=1;k<=t;k++)
 	 {cin>>c>>f>>x;
 	  //min=(x+f);
 	  minT=x;
 	  vector<double> a(int(x+2)); 
	  for(i=0;i<=x+1;i++)
	    {if(i!=0)
	       a[i]=a[i-1]+c/((i-1)*f+2);
	     minT=min(minT,a[i]+x/(i*f+2));
	    }
	  cout<<"Case #"<<k<<": ";
	  printf("%.7f\n",minT);
 	 }
 	
 }
