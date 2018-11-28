#include<stdio.h>

int main()
{
	int cases;
	int k = 0;
	
	scanf("%d",&cases);
	
	while(cases--)
	{
		double c=0,f=0,x=0;
		double t1=0,t2=0,t3=0,tb=0,tt=0;
		double r=2;
		int flag = 0;
		int flag1 = 1;
		
		scanf("%lf%lf%lf",&c,&f,&x);
		
		//time to reach X cookies with initial rate;
		t1 = (x/r);
		
		while(flag1 != 0)
		{
			//time to buy cookie farms
			tb = tb + (c/r);
			r = r+f;
			
			//time to reach X cookies with increased rate
			t2 = (x/r);
			t3 = tb + t2;
			
			if(t3<t1)
			{
				flag = 1;
				t1 = t3;
				tt = t3;
			}
			else
			flag1 = 0;
	    }		
	    
	    k++;
	    if(flag == 1)
	    printf("Case #%d: %lf",k,tt);
	    else if(flag == 0)
	    printf("Case #%d: %lf",k,t1);
	    
	    printf("\n");
		
	}
	return 0;
}
