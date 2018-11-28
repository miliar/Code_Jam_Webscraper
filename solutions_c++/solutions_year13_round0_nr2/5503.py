#include<iostream>
#include<iomanip>
#include<cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <string.h>

using namespace std;
#define f(i,a,b) for (int i = a; i < b; i++ )
#define rf(i,a,b) for (int i = a; i > =b; i-- )

int main()
{
	int t,n,m;
    	scanf("%d",&t);
    	for(int q=1;q<=t; q++)
    	{
    		scanf("%d%d",&n,&m);
    		int arr[n+1][m+1];
    		int flag=0;
    		memset(arr,0,sizeof(arr));
    		f(i,0,n)
    			f(j,0,m)
    			{
    				scanf("%d",&arr[i][j]);
    				if(arr[i][j]==1)
    				{
    					arr[i][m]++;
    					arr[n][j]++;
    				}
    			}
    		f(i,0,n)
    		{
    			f(j,0,m)
    			{
    				if(arr[i][j]==1)
    				{
    					if((arr[i][m]!=m)&&(arr[n][j]!=n))
    					{
    						printf("Case #%d: NO\n",q);
    						flag=1;
    						break;
    					}
    				}
    			}
    			if(flag)
    				break;
    		}
    		if(flag)
    			continue;
    		
    		printf("Case #%d: YES\n",q);
    		
    	}
}
