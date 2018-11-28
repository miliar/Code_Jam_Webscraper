#include<bits/stdc++.h>
#define mp make_pair
#define X first
#define Y second
using namespace std;
int shortest[1000005],rev;
queue<pair<int,int> >q;
void rever(int x)
{
    rev=0;
    while(x)
    {
        rev*=10;
        rev+=x%10;
        x/=10;
    }
}
int main()
{
    freopen("A-in.txt","r",stdin);
    freopen("A-out.txt","w",stdout);
    int t,cas,n;
    memset(shortest,-1,sizeof(shortest));
    q.push(mp(1,1));
    while(!q.empty())
    {
        if(q.front().X>1000000)
        {
            q.pop();
            break;
        }
        if(shortest[q.front().X]==-1)
        {
            shortest[q.front().X]=q.front().Y;
            q.push(mp(q.front().X+1,q.front().Y+1));
            rever(q.front().X);
            q.push(mp(rev,q.front().Y+1));
        }
        q.pop();
    }
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);
        printf("Case #%d: %d\n",cas,shortest[n]);
    }
}
