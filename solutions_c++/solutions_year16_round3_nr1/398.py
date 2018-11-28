#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    scanf("%d",&n);
    priority_queue<pair<int,int> > pq;
    int sum=0;
    for(int i=0;i<n;i++)
    {
        int t;
        scanf("%d",&t);
        sum+=t;
        pq.push(make_pair(t,i));
    }
    if(sum%2)
    {
        pair<int,int> a=pq.top();pq.pop();
        printf(" %c",a.second+'A');
        --a.first;
        if(a.first)    pq.push(a);
    }
    while(pq.size()>=2)
    {
        pair<int,int> a=pq.top();pq.pop();
        pair<int,int> b=pq.top();pq.pop();
        if(a.first==b.first)
        {
           printf(" %c%c",a.second+'A',b.second+'A');
            --a.first,--b.first;
            if(a.first)    pq.push(a);
            if(b.first)    pq.push(b);
        }
        else
        {
            printf(" %c%c",a.second+'A',a.second+'A');
            a.first-=2;
            if(a.first)    pq.push(a);
            pq.push(b);
        }
    }
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d:",i);
        solve();
        printf("\n");
    }
    return 0;
}
