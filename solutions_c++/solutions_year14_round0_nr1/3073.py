#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<cstring>
#include <cmath>
#include<algorithm>
#include<stack>
using namespace std;

int T;
int a;
int b;
int y[4];
int s[4][4];
int x[4];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a,in","w",stdout);
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&s[i][j]);
            }
        }
        for(int i=0;i<4;i++)
        {
            x[i]=s[a-1][i];
           // cout<<x[i]<<" ";
        }
       // cout<<endl;
        scanf("%d",&b);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&s[i][j]);
            }
        }
        for(int i=0;i<4;i++)
        {
            y[i]=s[b-1][i];
           // cout<<y[i]<<" ";
        }
       // cout<<endl;
        int ans=0;
        int cnt=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(x[i]==y[j])
                {
                    ans=x[i];
                    cnt++;
                    break;
                }
            }
        }
        if(cnt>1) printf("Case #%d: Bad magician!\n",i+1);
        else if(cnt==0) printf("Case #%d: Volunteer cheated!\n",i+1);
        else printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
