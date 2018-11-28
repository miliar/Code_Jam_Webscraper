#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
  int t;
  double c,f,x,p;
  int i,j;
  double k,k1;
  double t1,t2;
  cin>>t;
  for(i=0;i<t;i++)
{  
    cin>>c>>f>>x;
    k=0.000000;
    p=(c/(2+k));
    t1=0.000000;
    t2=0.000000;
    k1=1;
    while(1)
      {
      if(p+(x/(2+f+k))<(x/(2+k)))
	{
	  
	        t1=t1+p;
        	p=(c/(2+f+k));
		k=k1*f;
		k1++;


	}
      else
	{
	  t1=t1+(x/(2+k));
	  break;
	}
    }
	printf("Case #%d: %0.7lf\n",i+1,t1);

}
  return 0;
  
}

