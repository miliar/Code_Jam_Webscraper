#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t,ca=1;
	scanf("%d",&t);
	
	double c,f,x,t_prev,t_cur,time,sp;
	
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		sp=2.0;
		
		if(x<=c)
		{
			t_cur=x/sp;
			printf("Case #%d: %.7lf\n",ca,t_cur);
			ca++;
		    continue;
		}
		
		else
		{
			t_prev=x/sp;
			t_cur=x/sp;
			
			time=c/sp;
			
			while(t_cur<=t_prev)
			{	
				t_prev=t_cur;			
				sp=sp+f;
				t_cur=time+ x/sp;
				time+=c/sp;			
			    
			}
			
		}
		
		printf("Case #%d: %.7lf\n",ca,t_prev);		
				
		ca++;
	}
	return 0;
}				
				
			    	
			
			
		
		
		
		
		
		

		
