#include<cstdio>
#include<cstring>
int main(void)
{
    int T,N;
    int check;
    long long int temp,multi;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&N);
	printf("Case #%d: ",i);
        check=0;
        if(N)
	{
	    for(multi=1;;multi++)
	    {
	        temp=multi*N;
	        while(temp)
		{
		    check=check | (1 << temp%10);
		    temp/=10;
		}
		if(check==1023)
		    break;
	    }
	    printf("%lld\n",multi*N);
	}
	else
	    printf("INSOMNIA\n");
    }
    return 0;
}
