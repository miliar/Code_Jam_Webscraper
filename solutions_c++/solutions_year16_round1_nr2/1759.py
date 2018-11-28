#include <iostream>
#include<stdio.h>
using namespace std;
int a[52][52];
int b[1000][1000];

int main()
{
    freopen("input3.in","r",stdin);
    freopen("output3.txt","w",stdout);

    int t,n,c=1;;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",c);
        c++;
        int cnt[2502]={0};
        //cout<<cnt[0][2];
        scanf("%d",&n);
        int x=2*n-1;
        for(int i=0; i<x; i++)
        {
            for(int j=0; j<n; j++)
            {
                scanf("%d",&b[i][j]);
                cnt[b[i][j]]++;
              //  if(cnt[b[i][j]][j]>1) b[i][j]=INT_MAX;
            }
        }
        for(int i=1; i<=2500; i++)
        {
            if(cnt[i]%2!=0) printf ("%d ",i);
        }
        printf("\n");





    }
    return 0;
}
