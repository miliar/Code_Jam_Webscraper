#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,p;

	cin>>t;
	for(p=1;p<=t;p++)
	{
		double c,f,x,ans1=0,ans2=0,r=2,ans3=0;
		cin>>c>>f>>x;
		
		 while(1)
    	 {
    	 	 ans1=x/r;
    	 	 ans3=ans3+ans1;
    	 	 ans2+=c/r+(x/(r+f));
    	 	 if(ans3<=ans2)
    	 	 {
    	 	   printf("Case #%d: %.7lf\n",p,ans3);
       			break;
      		 }
      		else
      		{   
			  ans2-=x/(r+f);
        	  ans3+=c/r;
        	  ans3=ans3-ans1;
        	  r=r+f;
      		}
    	}
  	}	
	return 0;
}
