#include<stdio.h>
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,cse,t,a,b,k;
	int ans;
	scanf("%d",&t);
	for(cse=1;cse<=t;++cse)
	{
		scanf("%d%d%d",&a,&b,&k);
		ans = 0;
		for(i=0;i<a;++i)for(j=0;j<b;++j)
		if( (i&j) < k)++ans;
		printf("Case #%d: %d\n",cse,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
