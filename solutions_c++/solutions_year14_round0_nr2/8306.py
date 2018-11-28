#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int q,j;
	double x,c,f,rate,t,t1,t2,time;
	cin>>q;
	j=q;
	while(q!=0)
	{
	cin>>c>>f>>x;
	rate=2.0;
	t=0;
	int flag=0;
	time=x/rate;
	while(flag !=1)
			{
				t+=c/rate;
				rate+=f;
				t1=(c/rate) + (x/(rate+f));
				t2=x/rate;
				 if(t2<=t1)
				{
					t=t+t2;
					flag =1;
				}
			}
			if(t<time)
				printf("Case #%d: %.7lf\n",j-q+1,t);
			else
				printf("Case #%d: %.7lf\n",j-q+1,time);
			q--;
		}

return 0;
}


	
	
		
		
