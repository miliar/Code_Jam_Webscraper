#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin>>t;
    for(int in=1;in<=t;in++)
    {
    	double c,f,x,pr=2.0,t=0;
    	cin>>c>>f>>x; 
		double ans=x/2;
		if(x<=c)
		{
			printf("Case #%d: %0.7lf\n",in,(x/2));
			continue;
		}
    	while((x/(pr+f))<=((x-c)/pr))
    	{
    		double an;
    		t+=(c)/pr;
    		pr+=f;
    		an=t+(x)/pr;
    		ans=min(ans,an);
    	}   
    	printf("Case #%d: %0.7lf\n",in,ans);
    }
}

