#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
    int t,n,m;
    cin>>t;
    for(int kk=1;kk<=t;kk++)
    {
        cin>>n>>m;
        int a[n][m];
    	bool marked[n][m];
    	for(int i=0;i<n;i++)
    	{
    		for(int j=0;j<m;j++)
			cin>>a[i][j];
    	}
    	bool no=0,bb,b2;
    	for(int i=0;i<n;i++)
    	{
    		for(int j=0;j<m;j++)
    		{
    			bb=0;b2=0;
    			if(a[i][j]==1)
    			{
    				for(int k=0;k<n;k++)
    				{
    					if(a[k][j]!=1)
    					{
    						bb=1;
    						break;
    					}
    				}
    				for(int k=0;k<m;k++)
    				{
                        
    					if(a[i][k]!=1)
    					{
    						b2=1;
    						break;
    					}
    				}
    				if(bb && b2)
    				{
    					no=1;
    					break;
    				}
    			}
    		}
    	}
        if(no==1)
        printf("Case #%d: NO\n",kk);
        else
        printf("Case #%d: YES\n",kk);
    }
}
