#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int main()
{
	int t, i;
	double c, f, x, r[100], cl;
	cin>>t;
	if(t<1 || t>100)
		exit(0);
	for(i=0;i<t;i++)
	{	
		r[i]=0.0;
		cl=2.0;
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
		if(c>10000||c<1||f<1||f>100||x<1||x>1000000)
			exit(0);
		while(1)
		{
			if((x/cl)<((c/cl)+(x/(cl+f))))
			{	
				r[i]+=(x/cl);
				break;
			}
			else
			{	
				r[i]+=(c/cl);
				cl+=f;
			}
		}
	}
	for(i=0;i<t;i++)
		printf("Case #%d: %.7lf\n", i+1, r[i]);
	return 0;
}

			
						
