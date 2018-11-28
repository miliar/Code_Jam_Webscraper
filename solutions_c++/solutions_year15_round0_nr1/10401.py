#include<stdio.h>
#include<iostream>
#define in(x) scanf("%d",&x)
using namespace std;
int main()
{
    int t,n,s=0,i,j;
    char c;
in(t);
    for(j=1;j<=t;j++)
    {
        in(n);
	int count=0;
        scanf("%c",&c);
	scanf("%c",&c);		
        s=c-48;
        for(i=1;i<=n;i++)
        {
            scanf("%c",&c);
            if(s<i&&c!='0')
	     {
                 count+=(i-s);
		 s+=count;
	     }
	     s+=(c-48);
		 	
        }
        printf("Case #%d: %d\n",j,count);
    }
    return 0;
}
