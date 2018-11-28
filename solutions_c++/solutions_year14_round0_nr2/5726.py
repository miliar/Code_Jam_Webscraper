#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,k;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	cin>>t;
    for(k=1;k<=t;k++)	
	{
	 double c,f,x,d=2,result=0;
            cin>>c>>f>>x;
            while(1)
            {
                    if((c/d)+(x/(d+f)) < (x/(d)))
                    {
                       result=result+(c/d);
                       d=d+f;
                    }
                    else
                    {
                        result=result+(x/d); break;
                    }
            }
	
		 printf("Case #%d: %.7f\n",k,result);
 	}
return 0;		
}
