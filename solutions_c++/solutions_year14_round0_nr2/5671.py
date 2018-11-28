#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
//Google Code Jam'14 Qual - 2 (Small)
int main() 
{
	int t,tt;
	cin>>t;
	for(tt=1;tt<=t;tt++) 
	{
        double c,f,x,inc=2,ans=0;
        cin>>c>>f>>x;
        double ans1=ans+x/inc,ms;
        while(1) 
        {
          ans+=c/inc;
          inc+=f;
		  ms=ans+x/inc;
		  if(ms<ans1) 
           ans1=ms;
          else 
		   break;
	    }
		cout<<"Case #"<<tt<<": ";
		printf("%.7lf\n",ans1);
	}
	return 0;
}

