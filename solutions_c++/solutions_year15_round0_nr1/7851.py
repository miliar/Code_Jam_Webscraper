#include <stdio.h>
main(){
	//freopen("A-small-attempt5.in","r",stdin);
	int a,b,c[1001]={0},d,ans[1001]={0},f,sum=0;
	char g;
	scanf("%d",&a);
	for(b=0;b<a;b++)
	{
		scanf("%d",&f);
		for(d=0;d<=f;d++)
		{
			scanf(" %c",&g);
			c[d]=g-'0';			
		}
		for(d=0;d<=f;d++)
		{
			if(sum>=d)
				sum=sum+c[d];				
			else if(sum<d)
			{
			ans[b]++;	
			sum++;	
			d--;
			}
		}
		sum=0;
	}
 	freopen ("google.txt","w",stdout);
	for(d=0;d<a;d++)
		printf("Case #%d: %d\n",d+1,ans[d]);
	
}
