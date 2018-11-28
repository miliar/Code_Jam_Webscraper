#include<stdio.h>
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#define mod 1000000009
#define ll long long

using namespace std;

int main()
{
    int t,n,m,arr[100][100],maxx[100],maxy[100],x,flag,i,j;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for(x=0;x<t;x++)
    {
        scanf("%d%d", &n, &m);
        flag=0;
        for(i=0;i<100;i++)
        {
            maxx[i]=0;
            maxy[i]=0;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d", &arr[i][j]);
                if(arr[i][j]>maxx[i])
                    maxx[i]=arr[i][j];
                if(arr[i][j]>maxy[j])
                    maxy[j]=arr[i][j];
            }
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(arr[i][j]<maxx[i]&&arr[i][j]<maxy[j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag)
                break;
        }
        if(flag)
            printf("Case #%d: NO\n", x+1);
        else
            printf("Case #%d: YES\n", x+1);
    }
	return 0;
}
