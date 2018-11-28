#include <bits/stdc++.h>
using namespace std;


int inp[10005];

int main()
{

    freopen("0.in","r",stdin);
    freopen("ham.out","w",stdout);


	int a,b,c,d,e,x,y,z,n,k,test;

	scanf("%d",&test);

	for(int t=1;t<=test;t++)
	{

	    scanf("%d",&n);
	    for(a=0;a<n;a++)
	    {
	        scanf("%d",&inp[a]);
	    }
	    sort(inp,inp+n);
	    int mx=inp[n-1];

	    x=mx;

	    for(a=1;a<=mx;a++)
	    {
	        e=0;
	        for(b=0;b<n;b++)
	        {
	            if(inp[b]<=a) continue;
	            c=inp[b]/a;
	            if((inp[b]%a)) c++;
	            c--;
	            e=e+c;
	        }
	        x=min(x,e+a);
	    }
	    printf("Case #%d: %d\n",t,x);
	}


    return 0;
}
