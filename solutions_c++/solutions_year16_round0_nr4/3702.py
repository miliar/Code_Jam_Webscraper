#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    int arr[10];

    for(int k=1;k<=tc;k++)
    {
       int l,c,s;
       scanf("%d%d%d",&l,&c,&s);
       printf("Case #%d: ",k);
       for(int i=1;i<=s;i++)
       {
           printf("%d ",i);
       }
       printf("\n");
    }
    return 0;
}
