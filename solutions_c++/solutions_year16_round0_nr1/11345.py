#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
        freopen("A-small-attempt1.out","w",stdout);
    int cases=0,t;
    scanf("%d",&t);
    while(t--)
    {
        bool visited[10]={};
        int x,temp,i=1,n,counts=0;
        scanf("%d",&n);
        x=n;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",++cases);
            continue;
        }
        while(counts!=10)
        {
            temp=n;
            while(temp)
            {
                if(visited[temp%10]==false)
                    ++counts,visited[temp%10]=true;
                    temp=temp/10;
            }
            i++;
            n=x*i;
        }
        printf("Case #%d: %d\n",++cases,n-x);
    }
    return 0;
}

