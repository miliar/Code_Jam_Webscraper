#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	int j,t,i,k;
	float c,f,x;
	double val,ans,ansp,div,divc,at,divt;
	scanf("%d",&t);
	k=1;//printf("%.7f\n",500.0/6);
	while(t--)
	{
	    scanf("%f %f %f",&c,&f,&x);
	    ans=0;
	    ansp=0;
	    if(x<c)
	    val=x/2.0;
	    else
	    {
	      ansp=x/2.0;div=2.0;divc=0;
	       divt=c/div;
	       divc=divc+divt;
	       //printf("%.7f ",divt);
	          div=div+f;
	         // cout<<div<<" ";
	          at=x/div;
	          ans=divc+at;
	      while(ans<ansp)
	      {
	          ansp=ans;
	          divt=c/div;
	          divc=divc+divt;


	          div=div+f;
	          //cout<<div<<" ";
	          at=x/div;
	          ans=divc+at;
	      }
	      val=ansp;
	    }

        printf("Case #%d: %.7f\n",k,val);


	    k++;
     }
return 0;
}
