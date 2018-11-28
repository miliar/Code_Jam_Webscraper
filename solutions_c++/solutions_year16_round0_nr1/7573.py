#include<cstdio>
#include<climits>
using namespace std;
int main()
{
	int t,a,b,c,d,e,f=0;
	scanf("%d",&t);
	while(t--)
	{
		int A[10]={0};
		scanf("%d",&a);
        b=1;
        e=0;
        if(a==0)
        {
        	printf("Case #%d: insomnia\n",++f);
        }
        else
        {
        while((b*a)<=INT_MAX)
        {
        	c=b*a;
        	while(c>0)
        	{
               if(A[c%10]==0)
               {
               	e++;
               	A[c%10]=1;
               }
               c/=10;
        	}
        	if(e==10)
        	{
        		printf("Case #%d: %d\n",++f,b*a);
        		break;
        	}
        	b++;
        }
        if(e!=10)
        	printf("Case #1: insomnia\n",f);
        }
	}
	return 0;
}