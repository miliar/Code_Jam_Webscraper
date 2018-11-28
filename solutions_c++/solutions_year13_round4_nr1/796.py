#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
#include<cassert>
#include<set>
using namespace std;
#define gc getchar_unlocked
typedef long long int int64;
void scanint(int64 &x)
{
    register int64 c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,k,n,m,t,cnt=1,ans,o,e,p,ans1,kl,dis,cst,klt;
cin>>t;
set <int64> s;map <int64,int64> mp1,mp2;
set <int64> :: iterator it;
//priority_queue <pair <int64,int64> , vector < pair <int64,int64> >, greater < pair <int64,int64> > > pq;
vector < pair <int64,int64> > v;
while(t--)
{
cin>>n>>m;s.clear();mp1.clear();mp2.clear();v.clear();ans=ans1=0;
while(m--)
	{scanf("%lld %lld %lld",&o,&e,&p);
	dis = e-o;
	klt = p;
	cst = (dis*(n+n-dis+1))/2;
	ans = (ans+(((cst)%1000002013)*((klt)%1000002013))%1000002013)%1000002013;
	s.insert(o);s.insert(e);
	if(mp1.find(o)==mp1.end())mp1.insert(make_pair(o,p));else mp1[o]+=p;
	if(mp2.find(e)==mp2.end())mp2.insert(make_pair(e,p));else mp2[e]+=p;
	}
for(it=s.begin();it!=s.end();++it)
	{
	//cout<<(*it)<<" "<<mp1[(*it)]<<" "<<mp2[(*it)]<<endl;
	if(mp1[(*it)]>0)v.push_back(make_pair((*it),mp1[(*it)]));
	if(mp2[(*it)]>0)
		{
		kl = mp2[(*it)];
		for(i=v.size()-1;i>=0&&kl>0;i--)
			{
			dis = (*it)-v[i].first;
			cst = (dis*(n+n-dis+1))/2;
			klt = min(v[i].second,kl);
			//cout<<klt<<" "<<cst<<endl;
			ans1 = (ans1+(((klt)%1000002013)*((cst)%1000002013))%1000002013)%1000002013;
			kl-=klt;
			v[i].second-=klt;
			}
		}
	}
ans = ans-ans1;
if(ans<0)ans+=1000002013;
printf("Case #%lld: %lld\n",cnt,ans);
cnt++;
}
return 0;
}


