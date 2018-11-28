#include<iostream>
#include<stdio.h>
using namespace std;
int matrix[100][100];
#define min(a,b) a<b?a:b
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,tc,i,j,n,m,max,savei,savej,flag,temp;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        flag=1;
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                scanf("%d",&matrix[i][j]);
        max=0;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(max<matrix[i][j])
                {
                    max=matrix[i][j];
                    savei=i;   savej=j;
                }
        for(i=0;i<n;i++)
        {
            if(i==savei) continue;
            for(j=0;j<m;j++)
            {
                if(j==savej)continue;
                temp=min(matrix[savei][j],matrix[i][savej]);
                if(matrix[i][j]!=temp)
                {
                      flag=0;
                      //cout<<i<<j<<endl;
                      //cout<<matrix[i][j]<<" ";
                      //cout<<temp<<endl;
                }
            }
        }
        if(flag)
           printf("Case #%d: YES\n",tc);
        else
           printf("Case #%d: NO\n",tc);
    }
    return 0;
}
 //display
        /*for(i=0;i<n;i++){
            for(j=0;j<m;j++)
                printf("%d ",matrix[i][j]);cout<<endl;}*/
