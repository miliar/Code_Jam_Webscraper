#include<cstdio>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	double prev_c,prev_ans,curr_ans,curr_x,x,c,f,var,rate,ans;
	int t,p=1;
	scanf("%d",&t);
	while(t--)
	{
		int px=0;
		rate=2;
		var=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		prev_c=c/rate;
		ans=prev_ans=x/rate;
		rate+=f;
		while(1)
		{
			var+=(prev_c);
			curr_ans=var+ (x/rate);
			if(curr_ans>prev_ans)
			{
				ans=prev_ans;
				break;
			}
			else
				prev_ans=curr_ans;
			prev_c=(c/rate);
			rate+=f;	
			
		}
		printf("Case #%d: %.8lf\n",p++,ans);
	}
	return 0;
}
			
