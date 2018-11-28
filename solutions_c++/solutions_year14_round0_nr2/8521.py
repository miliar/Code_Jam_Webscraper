#include<iostream>
//#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define mod 1000000007
#include <vector>

using namespace std;

int main()
{
	freopen("D:/in.txt","r",stdin);
   freopen("D:/out.txt","w",stdout);
   int t,i,j,n;
	double c,f,x,time,tmp,tm,r;

	scanf("%d",&t);
    for(int tc=1;tc<=t;++tc)
    {
       scanf("%lf%lf%lf",&c,&f,&x);
       r=2;
       time=x/r; //cout<<time<<endl;
       tmp=0;
       while(1)
       {
          tmp+=c/r;
          tm=tmp;
          r+=f;
          tmp+=x/r; //cout<<tmp<<endl;
          if(tmp>time)
            break;
          else
          {
            time=tmp;
            tmp=tm; //tmp-=x/r;
          }
       }

       printf("Case #%d: %0.7f\n",tc,time);

    }

	return 0;

}
