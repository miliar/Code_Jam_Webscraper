#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>

using namespace std;

const int maxn = 12;
const int inf = 1<<29;

map<int,int> mp;
map<int,int> ::iterator it;

int data[maxn],n,tp[maxn];
int pai[maxn],res;

void check()
{
    int pt ;
    for(int i=1;i<=n;i++)
        if(pai[i]==n)
        {
            pt = i;
            break;
        }
    for(int i=1;i<pt;i++)
        if(pai[i]>pai[i+1])
            return;
    for(int i=pt+1;i<=n;i++)
        if(pai[i]>pai[i-1])
            return;
    for(int i=1;i<=n;i++)
        tp[i] = data[i];
    int cnt = 0;
    for(int i=1;i<=n;i++)
    {
        int pt;
        for(int j=i;j<=n;j++)
        {
            if(tp[j]==pai[i])
            {
                pt  = j;
                break;
            }
        }
        for(int j=pt-1;j>=i;j--)
        {
            cnt++;
            swap(tp[j],tp[j+1]);
        }
    }
    res = min(res,cnt);
}
int sol()
{
    res = inf;
    for(int i=1;i<=n;i++)
        pai[i]  = i;
    do
    {
        check();
    }while(next_permutation(pai+1,pai+n+1));
    return res;
}
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        mp.clear();scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",data+i);
            mp[data[i]];
        }
        int tot = 0;
        for(it=mp.begin();it!=mp.end();it++)
            it->second = ++tot;
        for(int i=1;i<=n;i++)
            data[i] = mp[data[i]];
        printf("Case #%d: %d\n",++cas,sol());
    }
}
