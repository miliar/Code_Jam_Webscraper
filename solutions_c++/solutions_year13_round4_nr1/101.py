#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
#define ll long long
const long long LINF = ~(((long long)0x1)<<63)/2;
const int INF=0X3F3F3F3F;
const double eps=1e-7;
const int MOD=1000002013;
struct Node
{
    int l,r,num;
}node[1500];
vector<int> a;
ll cnt[3000];
int main()
{
    int T;
    freopen("A-small-attempt0.in.txt","r",stdin);
    freopen("A-small-attempt0.out.txt","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        ll n;
        cin>>n;
        int m;
        ll pay=0;
        scanf("%d",&m);
        a.clear();
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<m;i++)
        {
            scanf("%d%d%d",&node[i].l,&node[i].r,&node[i].num);
            a.push_back(node[i].l);
            a.push_back(node[i].r);
            if(node[i].l!=node[i].r)
            {
                pay+=(n+(n-(node[i].r-node[i].l-1)))*(node[i].r-node[i].l)/2*node[i].num;
                //   cout<<pay<<endl;
            }
        }
        sort(a.begin(),a.end());
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<a.size()-1;j++)
                if(node[i].l<=a[j]&&a[j+1]<=node[i].r)
                    cnt[j]+=node[i].num;
        }
        ll ans=0;
        //   for(int i=0;i<a.size()-1;i++)
        //     cout<<cnt[i]<<endl;
        for(int i=0;i<a.size()-1;i++)
            while(cnt[i])
            {
                ll num=LINF;
                int id=a.size()-2;
                for(int j=i;j<a.size()-1;j++)
                {
                    if(!cnt[j])
                    {
                        id=j-1;
                        break;
                    }
                    num=min(num,cnt[j]);
                }
                ll value=0;
                int p=0;
                for(int j=i;j<=id;j++)
                {
                    cnt[j]-=num;
                }
                
                int l=a[i],r=a[id+1];
                //  cout<<l<<" "<<r<<endl;
                if(l==r) continue;
                value+=(n+(n-(r-l-1)))*(r-l)/2;
                //   cout<<id<<" "<<value<<" "<<num<<endl;
                ans+=value*num;
            }
        printf("Case #%d: ",cas);
        //  cout<<pay<<" "<<ans<<endl;
        cout<<pay-ans<<endl;
        
    }
    return 0;
}








