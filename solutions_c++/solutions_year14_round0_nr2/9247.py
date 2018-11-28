#include<iostream>
#include <fstream>
#include <cstdio>
#include<cstring>
using namespace std;
int main()
{
	int t,in;

	freopen("B-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
scanf("%d",&t);
    for(in=1;in<=t;in++)	
	{
	 double c,f,x,d=2,ans=0;
            cin>>c>>f>>x;
            while(1)
            {
                    if((c/d)+(x/(d+f)) < (x/(d)))
                    {ans = ans +(c/d);d=d+f;}
                    else
                    {ans = ans +(x/d); break;}
            }
	
		 printf("Case #%d: %.7f\n",in,ans);
 	}
return 0;		
}
