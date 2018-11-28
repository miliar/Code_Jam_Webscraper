#include<bits/stdc++.h>
using namespace std;
std::queue<int>q;
int func(int x)
{
    int cnt=0,temp;
    while(!q.empty())
    {
     temp=q.front();
     q.pop();
     if(temp>x)
     {
        if(temp-x>x)
            q.push(temp-x);
        cnt++;
        }
    }
return cnt;
}

int t,X,i,j,a[1005],ans,n;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);

    while(t--)
    {X++;
    ans=10;
        scanf("%d",&n);

        for(i=0; i<n; i++)
        scanf("%d",&a[i]);

        for(i=1;i<=9;i++)
        {
            while(!q.empty())
                q.pop();
            for(j=0;j<n;j++)
            q.push(a[j]);
            ans=min(ans,func(i)+i);
        }
        printf("Case #%d: %d\n",X,ans);
    }
    return 0;
}
