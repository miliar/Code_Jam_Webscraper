#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
#define F(i,n) for(i=0;i<n;i++)
using namespace std;
int main()
{
	int t,n,m,a[111][111],i,l,r,tmp,j,flag;
	cin>>t;
	for(l=1;l<=t;l++)
	{   
	    //memset(r,0,sizeof(r));
	    cin>>n>>m;
		for(i=0;i<(n);i++)
		{for(j=0;j<m;j++)
		  scanf("%d",&a[i][j]);
		}
		F(i,n)
		{ 
		F(j,m)
		{ 	flag=0;
			for(r=0;r<m;r++)
		     if(a[i][j]<a[i][r])
		      {flag=1;break;}
		      if(flag==1)	   
			 {   //cout<<a[i][j]<<endl;
					for(r=0;r<n;r++)
					{//cout<<a[i][j]<<" "<<a[r][j]<<endl;
						if(a[i][j]<a[r][j])
					{ printf("Case #%d: NO\n",l);
					  goto X;
					}
				}
								
			} 
		}
	}
	 printf("Case #%d: YES\n",l);
	 X:;
 }
		return 0;
	}
