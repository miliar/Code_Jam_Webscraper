#include <bits/stdc++.h>
using namespace std;

int mx[20];
int my[20];

int grid[20][20];

void clr(int r,int c)
{
    int i,j;
    for(i=0;i<=r;i++)
    {
        for(j=0;j<=c;j++) grid[i][j]=0;
    }
}

int calc(int r,int c)
{
    int i,j,k,cnt;
    cnt=0;
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(i+1<r)
            {
                if(grid[i][j] && grid[i+1][j]) cnt++;
            }
            if(j+1<c)
            {
                if(grid[i][j] && grid[i][j+1]) cnt++;
            }
        }
    }
    return cnt;
}

int main()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);


	int it,T;

    int ans;
    int i,j,k,cnt,r,c,n,x,y;
	scanf("%d",&T);

	for(it=1;it<=T;it++)
	{


	    scanf("%d%d%d",&r,&c,&k);

	    n=r*c;

	    clr(r,c);

	    cnt=0;
	    for(i=0;i<r;i++)
	    {
	        for(j=0;j<c;j++)
	        {
	            mx[cnt]=i;
	            my[cnt]=j;
	            cnt++;
	        }
	    }

	    ans=r*r*c*c;

	    for(i=0;i<(1<<n);i++)
	    {
	        cnt=0;
	        for(j=0;j<n;j++)
	        {
	            if((i&(1<<j))) cnt++;
	        }
	        if(cnt==k)
	        {
	            clr(r,c);
	            for(j=0;j<n;j++)
                {
                    if((i&(1<<j)))
                    {
                        x=mx[j];
                        y=my[j];
                        grid[x][y]=1;
                    }
                }
                ans=min(ans,calc(r,c));
	        }
	    }
	    printf("Case #%d: %d\n",it,ans);


	}

    return 0;
}
