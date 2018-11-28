#include <iostream>
#include <algorithm>
#include <sstream>
#include<math.h>
#include<stdio.h>

using namespace std;

int main( )
{
    int num,a[110][110],n,m,t,i,j,k,y=0,p,max=0;
    cin >> t;
    for(k=1;k<=t;k++)
    {
        cin >> n >> m;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                cin >> a[i][j];
                if(a[i][j]>max)
                {
                    max=a[i][j];
                    a[i][100]=max;

                }

            }
            max=0;
        }

    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]!=a[i][100])
            {
                for(p=0;p<n;p++)
                {
                    if(a[p][j]>a[i][j])
                    {
                        y=1;
                        goto e;
                    }
                }
            }
        }
    }
    e:
    if(y==0)
    printf("Case #%d: YES\n",k);
    else
    printf("Case #%d: NO\n",k);
    y=0;
    for(i=0;i<100;i++)
    a[i][101]=0;

    }



 }

