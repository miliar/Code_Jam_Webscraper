# include<stdio.h>
int fun(int n)
{
    int i,l,f=0,s1,s2,k;
    for(i=1;i<100;i++)
    {
        if(i*i==n)
        {
            l=i;
			f=1;
            break;
        }
    }
	s1=l;s2=0;
	if(f==1)
	{
		while(s1>0)
		{
			k=s1%10;
			s2=s2*10+k;
			s1=s1/10;
		}
		if(s2==l)
			return 1;
		else
			return 0;
	}
	return 0;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int t=0,T,a,b;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",++t);
        scanf("%d%d",&a,&b);
        int count=0,i,s1,s2,k;
        for(i=a;i<=b;i++)
        {
            s1=i;
            s2=0;
            while(s1>0)
            {
                k=s1%10;
                s2=s2*10+k;
                s1=s1/10;
            }
			//printf("%d",s2);
            if(s2==i&&fun(s2))
            {
				//printf("%d ",s2);
                count++;
            }
        }
        printf("%d\n",count);
    }
    return 0;
}
