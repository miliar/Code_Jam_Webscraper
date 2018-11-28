#include <bits/stdc++.h>
using namespace std;

const int N=1010;
int cnt[N];

vector<int> pan;
int getmax()
{
    int s=0;
    for(int i=0;i<pan.size();i++)
        s=max(s, pan[i]);
    return s;
}
int ans;

const int low[]={0,1,2,3,3,4,4,5,5,6};
void decrease()
{
    for(int i=0;i<pan.size();i++)
        pan[i]--;
}

void increase()
{
    for(int i=0;i<pan.size();i++)
        pan[i]++;
}

void divide(int i, int to, int val)
{
    pan[i]-=val;
    if(i == to)
        pan.push_back(val);
    else
        pan[to]+=val;
}

void combine(int i, int to, int val)
{
    pan[i]+=val;
    if(i == to)
        pan.pop_back();
    else
        pan[to]-=val;
}

void opvect()
{
    for(int i=0;i<pan.size();i++)
        printf("%d ",pan[i]);
    printf("\n");
}

bool impossible(int t)
{
    int x=getmax();
    int n=0;
    for(int i=0;i<pan.size();i++)
        if(x==pan[i])
        n++;
    int y=n-1+low[x];
    return t+y>=ans&&t+x>=ans;
}
void dfs(int t)
{
 //   opvect();
    if(impossible(t))
    {
        return;
    }

    int maxv=getmax();
    if(maxv<=3)
    {
   //     printf("%d %d\n",t,maxv);
        ans=min(ans, t+maxv);
        return;
    }
    if(maxv>9) return;
    decrease();
    dfs(t+1);
    increase();
    bool v[60]={false};
    for(int i=0;i<pan.size();i++)
    {
        if(pan[i]<=0) continue;
        if(v[pan[i]]) continue;
        v[pan[i]] = true;
        if(pan[i]>=4)
        {
            for(int j=0;j<pan.size();j++)
                for(int val=1;val<=pan[i];val++)
                {
                    divide(i, j, val);
                    dfs(t+1);
                    combine(i, j, val);
                }
        }
    }
}
int main()
{
    freopen("B5.in","r",stdin);
    freopen("out5.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        pan.clear();
        memset(cnt,0,sizeof(cnt));
        int n;
        scanf("%d",&n);
   //     printf("%d\n",n);
        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
    //        printf("%d ",x);
            pan.push_back(x);
            cnt[x]++;
        }
    //    printf("\n");
        ans=getmax();
        dfs(0);
//        int ans=1000;
//        int special = 0;
//        for(int i=1000;i>0;i--)
//        {
//            if(!cnt[i])
//                continue;
//            int tmp=i+special;
//            ans=min(ans,tmp);
//            cnt[i/2]+=cnt[i];
//            cnt[i-i/2]+=cnt[i];
//            special+=cnt[i];
//        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}
