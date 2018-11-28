#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    int smax;int mcount=0,need=0,i,count=1;
    char arr[1055];
    freopen("A-large.in","r",stdin);
    freopen("ans.txt", "w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        cin>>smax;
        cin>>arr;
        mcount=arr[0]-48;
        for(i=1;i<=smax;i++)
        {
            if(mcount<i && arr[i]){need=need+(i-mcount);mcount=mcount+(i-mcount);}
            mcount=mcount+(arr[i]-48);
        }
        printf("Case #%d: %d\n",count,need);
        count++;
        need=0;mcount=0;
    }
    return 0;
}
