#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include<iostream>
#define MAX 1004
using namespace std;
double A[MAX],B[MAX];
int n;
int Deceitful_War()
{
    int ans=0;
    int o=n;
    int i,j;
    i=n-1;
    j=n-1;
    while(o>0)
    {
        if(A[i]>B[j])
            ans++,i--,j--,o--;
        else
        {
            j--,o--;
        }
    }

    return ans;
}
int War ()
{
    int ans=0;
    bool vis[MAX];
    fill(&vis[0],&vis[MAX],false);
    for(int i = 0 ; i < n ; i++)
    {
        bool found=false;
        for(int j = 0 ; j  < n ; j++)
        {

            if(B[j]>A[i] && !vis[j])
            {
                vis[j]=1;
                found = true;
                break;
            }
        }
        if(!found)
        {
            for(int j = 0 ; j  < n ; j++)
            {
                if(!vis[j])
                {
                    vis[j]=1;
                    break;
                }
            }
            ans++;

        }
    }
    return ans;
}
int main()
{
    freopen("S.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int g=1;
    while(t--)
    {
        scanf("%d",&n);
        for (int i=0; i<n; i++)
            scanf("%lf",&A[i]);
        for (int i=0; i<n; i++)
            scanf("%lf",&B[i]);
        sort(A,A+n);
        sort(B,B+n);
        printf("Case #%d: %d %d\n",g++,Deceitful_War(),War());
    }
}
