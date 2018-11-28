#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
typedef long long ll;
using namespace std;
int matrix[105][105],maxr[105],maxc[105],res[105][105];
int main()
{
    int t,i,j,n,m,flag=0,counter=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        counter++;
        flag=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        scanf("%d",&matrix[i][j]);
        for(i=0; i<n; i++)
        maxr[i]=INT_MIN;
        for(j=0;j<m;j++)
        maxc[j]=INT_MIN;
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        if(maxr[i]<matrix[i][j])maxr[i]=matrix[i][j];
        for(j=0;j<m;j++)
        for(i=0;i<n;i++)
        if(maxc[j]<matrix[i][j])maxc[j]=matrix[i][j];
        //row insert
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
            res[i][j]=maxr[i];
        //column insert
        for(j=0;j<m;j++)
            for(i=0;i<n;i++)
                if(res[i][j]>maxc[j])res[i][j]=maxc[j];
        //checking....
        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
                if(res[i][j]!=matrix[i][j])
                flag=1;
        if(flag)
        printf("Case #%d: NO\n",counter);
        else
        printf("Case #%d: YES\n",counter);
    }
    return 0;
}
