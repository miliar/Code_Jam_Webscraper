#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
using namespace std;
#define maxn 2300
struct Pas
{
       int l,r,x;
}e[maxn];
int wx[maxn];
int i,j,k;
int tst,cas;
int n,m;
map<int,bool> mp;
map<int,bool>::iterator it;
int l,r,x;
void Ins(int x)
{
     if (mp.find(x)==mp.end()) mp.insert(pair<int,bool>(x,0));
}
long long cal(int x)
{
     long long ret;
     ret=(long long)(((x-1)*x)>>1);
     return ret;
}
long long ans;
int mi;
int hd[maxn];
int main()
{
    cin>>tst;
    for (cas=1;cas<=tst;cas++)
    {
        cin>>m>>n;
        mp.clear();
        ans=0;
        for (i=0;i<n;i++)
        {
            cin>>e[i].l>>e[i].r>>e[i].x;
            Ins(e[i].l);
            Ins(e[i].r);
            ans-=cal(e[i].r-e[i].l)*e[i].x;
        }
        m=0;
        for (it=mp.begin();it!=mp.end();it++) wx[m++]=it->first;
        memset(hd,0,sizeof(hd));
        for (i=0;i<m-1;i++)
        {
            for (j=0;j<n;j++)
                if (e[j].l<=wx[i] && e[j].r>=wx[i+1]) hd[i]+=e[j].x;
        }
        for (i=0;i<m-1;)
        {
            while (hd[i]==0 && i<m) i++;
            if (i>=m) break;
            l=wx[i];
            mi=0x7fffffff;
            for (j=i;j<m;j++)
            {
                if (hd[j]==0) break;
                if (mi>hd[j]) mi=hd[j];
            }
            for (k=i;k<j;k++)
            {
                hd[k]-=mi;
            }
            r=wx[j];
            ans+=cal(r-l)*mi;
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
//    system("PAUSE");
    return 0;
}
