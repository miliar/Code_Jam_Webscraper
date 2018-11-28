#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
#include<map>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-0.out","w",stdout);
    int t,ti;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        int adj[4][4];
        int r1,r2,i,j;
        scanf("%d",&r1);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>adj[i][j];
            int ar[17]={0};
        for(j=0;j<4;j++){
            ar[adj[r1-1][j]]=1;
            }
        scanf("%d",&r2);
        int noc=0,ans;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>adj[i][j];
        for(j=0;j<4;j++)
        {
        	//cout<<adj[r1-1][j]<<",";
            if(ar[adj[r2-1][j]]==1){ ans=adj[r2-1][j];
                noc++;}
        }
        if(noc==1)
        {
            printf("\nCase #%d: %d",ti,ans);
        }
        else if(noc>1)
        {
            printf("\nCase #%d: Bad magician!",ti);
        }
        else
        {
            printf("\nCase #%d: Volunteer cheated!",ti);
        }
    }
    return 0;
}
