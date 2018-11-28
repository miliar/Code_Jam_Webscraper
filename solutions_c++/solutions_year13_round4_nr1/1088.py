#include<iostream>
#include<cstring>
#include<cstdio>
#include<queue>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<functional>
using namespace std;
typedef long long int64;
int64 n,m;
int64 ans;
int64 cal(int64 len)
{
    return (n+n-len+1)*len/2;
}
const int64 mod=1000002013;
void dos(vector< pair< pair<int,int> ,int> >ff)
{
    int i,j,k;
    if(ff.size()==0)
      return;
    if(ff.size()==1)
    {
        ans+= cal(ff[0].first.second-ff[0].first.first)%mod*ff[0].second%mod;
        ans%=mod;
        return;
    }
    for(i=1;i<ff.size();i++)
     if(ff[i].first.first>ff[i-1].first.second)
        break;
      if(i<ff.size())
      {
         vector< pair< pair<int,int> ,int> > aa,bb;
         for(j=0;j<i;j++)
           aa.push_back(ff[j]);
         for(j=i;j<ff.size();j++)
           bb.push_back(ff[j]);
        dos(aa);
         dos(bb);
         return;
        }
      int64 mn=1000000000;
      mn*=mn;
      for(i=0;i<ff.size();i++)
        mn=min(mn,(int64)ff[i].second);
      
      vector< pair< pair<int,int> ,int> > tt;
      ans+=cal(ff[ff.size()-1].first.second-ff[0].first.first)%mod*mn;
      ans%=mod;
      for(i=0;i<ff.size();i++)
      {
         pair< pair<int,int> ,int> dd=ff[i];
         dd.second-=mn;
         if(dd.second>0)
           tt.push_back(dd);
           
        }
        if(tt.size())
          dos(tt);
      
}
map<int,int> mp;
vector<int> ee,uu;
int rt[10000];
int main()
{
    int cas;
    cin>>cas;
    int cc=0;
    mp.clear();
    while(cas--)
    {
        mp.clear();
        ans=0;
        cin>>n>>m;
       vector<pair< pair<int,int> ,int> >gg,ww;
       int64 tot=0;
       ee.clear();
       uu.clear();
       for(int i=0;i<m;i++)
       {
             pair< pair<int,int> ,int> a;
             scanf("%d%d%d",&a.first.first,&a.first.second,&a.second);
             gg.push_back(a);
             ee.push_back(a.first.first);
             ee.push_back(a.first.second);
             tot+=cal(a.first.second-a.first.first)%mod*a.second;
             tot%=mod;
        }
        sort(ee.begin(),ee.end());
        int cur=0;
        for(int i=0;i<ee.size();i++)
         if(mp.find(ee[i])==mp.end())
         {
           mp[ee[i]]=++cur;
           rt[cur]=ee[i];
        }
        pair< pair<int,int> ,int> fy;
        map< pair<int,int> ,int > ss;
        for(int i=0;i<gg.size();i++)
        {
            fy.second=gg[i].second;
            int st=mp[gg[i].first.first];
            int ed=mp[gg[i].first.second];
            for(int j=st+1;j<=ed;j++)
            {
                fy.first.first=rt[j-1];
                fy.first.second=rt[j];
                ss[fy.first]+=fy.second;
            }
        }
        map<pair<int,int>,int >::iterator p=ss.begin();
        while(p!=ss.end())
        {
            fy.first=p->first;
            fy.second=p->second;
            ww.push_back(fy);
            p++;
        }
        dos(ww);
       // cout<<tot<<" "<<ans<<endl;
        if(ans<=tot)
          ans=tot-ans;
        else
        {
          ans=tot-ans;
          while(ans<0)
            ans+=mod;
        }
         cout<<"Case #"<<++cc<<": "<<ans<<endl;
    }
    return 0;
}
