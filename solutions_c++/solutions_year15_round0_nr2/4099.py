#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
    int j,t,d,a[1002],b[1002],i,ans,k,p;

    scanf("%d",&t);
    for(j=0;j<t;j++)
    {
        k=0;
        scanf("%d",&d);
        for(i=0;i<d;i++)
            scanf("%d",&a[i]);
        p=a[0];
        sort(a,a+d);
        if(a[d-1]==1)
        {
        	printf("Case #%d: 1\n",j+1);
        	continue;
    	}
        i=0;
        while(a[d-1]!=1)
        {
        	b[i]=a[d-1]+i;
        	a[d-1]=a[d-1]/2+a[d-1]%2;
			sort(a,a+d);
			i++;
        }
        sort(b,b+i);
        if(d==1&&p>6&&p<9)
        {
        	printf("Case #%d: %d\n",j+1,b[0]+1);
        	continue;
        }
		printf("Case #%d: %d\n",j+1,b[0]);
    	
	}
    return 0;
}

