using namespace std;
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define wl(n) while(n--)
#define ll long long
#define bitcnt(x) __builtin_popcount(x)
#define P(x) printf("%d\n",x)
#define PB push_back
#define MP make_pair
#define fl(i,n) for(i=0;i<n;i++)
#define fil(i,a,n) for(i=a;i<n;i++)
#define rev(i,a,n) for(i=n-1;i>=a;i--)
#define mem(a,i) memset(a,i,sizeof(a))
#define F first
#define S1 second
typedef pair<int,int> P;
vector<int> v1;
pair<int,int> p1;
#define MOD 1000000007
#define debug(x)  printf("####%d####\n",x);
#define nl printf("\n");
#define str string
int a[1234567];
string s,s1;
int dp[103][5][5];
ll pow1(ll x,ll y)
{
    if(y==0)
    return 1;
    ll temp= pow1(x,y/2)%MOD;
    if(y%2==0)
    return (temp*temp)%MOD;
    else
    return (((temp*temp)%MOD)*x)%MOD;
}
// int flick(int,int);
// int fluck(string s);
// int flick(int i,int n)
// {
//  string s2="";
//  int j;
//  fl(j,i+1)
//      s2+=s[j];
//  reverse(s2.begin(), s2.end());
//  fl(j,i+1)
//  {
//      if(s2[j]=='+')
//          s2[j]='-';
//      else
//          s2[j]='+';
//  }
//  for(j=i+1;j<n;j++)
//      s2+=s[j];
//  return fluck(s2);
// }
// int func(int count,int f,int g)
// {
//  // cout<<count<<" "<<f<<" "<<g<<"\n";
//  if(count==1)
//  {
//      if(g==0)
//      {
//          if(f==1)
//          return 0;
//          return 1;
//      }
//  }
//  int &ans=dp[count][f][g];
//  if(ans!=-1)
//      return ans;
//  ans=1e9;
//  int f1=count,f2=count-1;
//  if(g)
//      f2++;
//  s="";
//  if(f==1)
//  {
//      while(f1>0&&f2>0)
//      {
//          s+='+';
//          s+='-';
//          f1--;
//          f2--;
//      }
//      if(f1)
//          s+='+';
//  }
//  else
//  {
//      while(f1>0&&f2>0)
//      {
//          s+='-';
//          s+='+';
//          f1--;
//          f2--;
//      }
//      if(f1)
//          s+='-';
//  }
//  int i,n=s.length();
//      fl(i,n)
//          ans=min(ans,1+flick(i,n));
//  return ans;
// }
int fluck(string s)
{
    s1="";
    int i,f,n=s.length();
    s1+=s[0];
    fil(i,1,n)
    {
        if(s[i]!=s[i-1])
            s1+=s[i];
    }
    s=s1;
    n=s.length();
    int c1=0;
    fl(i,n)
    {
        if(s[i]=='-')
            c1++;
    }
    if(s[0]=='+')
        return 2*c1;
    else
        return 2*c1-1;
}
int main()
{
    //std::ios_base::sync_with_stdio(false);
    int t;
    int n,i,j,k,m,l,f;
    // freopen("/home/meintoo/Downloads/input.txt","r",stdin);
    // freopen("/home/meintoo/Downloads/output.txt","w",stdout);
    S(t);
    l=1;
    wl(t)
    {
        cin>>s;
        int ans=fluck(s);
        printf("Case #%d: %d\n",l++,ans);
    }
    return 0;
}