#include <bits/stdc++.h>

#define rep(i,n) for(i=0;i<n;i++)
#define ll long long 
#define elif else if
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
using namespace std;

int ans=99999999;
map<vector<int>, int>myp;
int foo( vector<int>v)
{
   sort(v.begin(),v.end());
   int i,l=v.size();
   /*cout<<"\n";
   for(i=0;i<l;i++)
    cout<<v[i]<<" ";*/
   if(l==0)
   {
    return 0;
     }
    if(myp.find(v)!=myp.end())
    {
      return myp[v];
    } 
   vector<int>tem;
   int an=99999999;
   for(i=0;i<l;i++)
   {
    if(v[i]>1)tem.pb(v[i]-1);
   }
   an=min(foo(tem)+1,an);
   for(i=0;i<l;i++)
   {
    if(v[i]>1)
    {
       int k;
       for(k=1;k<=v[i]/2;k++)
       {
       vector<int>te(v);
       te.erase(te.begin()+i,te.begin()+i+1);
       te.pb(k);
       te.pb(v[i]-k);
       an=min(an,1+foo(te));
       }
           }
   }
   myp[v]=an;
   return an;
}
int main()
{
  freopen("int","r",stdin);
  freopen("out","w",stdout);
	int T,t;
	cin>>T;
	for (t=1;t<=T;t++)
	{
    myp.clear();
    ans=99999999;
    vector<int>v;
    int i,j,n,num;
    string st;
    cin>>n;
    int te=0;
    rep(i,n)
    {
      cin>>num;
        v.pb(num);
       
      //if(t==19)cout<<num<<" ";
    }
    /*int l=v.size();
    while(1)
    {
      sort(v.begin(),v.end());
      l=v.size();
      if(v[l-1]<=2)
        break;
      num=v[l-1];
      int div=num/2;
      v.erase(v.end()-1,v.end());
      v.pb(num-div);
      v.pb(div);
      ans++;
      //cout<<num<<" ";
    }
    ans+=v[v.size()-1];*/
    ans=foo(v);
    printf("Case #%d: %d\n",t,ans);
	}
  //Case #1: 0	
	return 0;
}