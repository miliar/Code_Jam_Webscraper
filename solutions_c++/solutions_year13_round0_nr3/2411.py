#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
using namespace std;
typedef long long int int64;
int64 palin(int64 a)
{
vector <int64> v;
int64 i,k,j;
while(a>0){v.push_back(a%10);a/=10;}
for(i=0,j=v.size()-1;i<v.size();i++,j--)if(v[i]!=v[j])return 0;
return 1;
}
int64 sqr(int64 a)
{
int64 b=sqrt(a);
if(b*b==a)return 1;
else return 0;
}
int main()
{
//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
int64 i,j,k,t,n,m,fl,cnt=1,l,r,ans;
vector <int64> an;
for(i=1;i<=10000000;i++)
	{
	if(palin(i))
		{
		if(palin(i*i))an.push_back(i*i);
		}
	}
//sort(an.begin(),an.end());
//cout<<an.size();
//for(i=0;i<an.size();i++)cout<<an[i]<<endl;
cin>>t;
while(t--)
{
scanf("%lld %lld",&l,&r);ans=0;
for(i=0;i<an.size();i++)if(an[i]>=l&&an[i]<=r)ans++;
printf("Case #%lld: %lld\n",cnt,ans);
cnt++;
}
return 0;
}
