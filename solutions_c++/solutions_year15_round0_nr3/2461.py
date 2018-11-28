#include <bits/stdc++.h>

#define rep(i,n) for(i=0;i<n;i++)
#define ll long long 
#define elif else if
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
using namespace std;

int mat[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
int mul(int a, int b)
{
  int ans=mat[abs(a)-1][abs(b)-1];
  if(a<0 || b<0)
    ans= -1*ans;
  return ans;
}
int tell( char c)
{
  if(c=='i')
    return 2;
  if(c=='j')
    return 3;
  if(c=='1')
    return 1;
  return 4;
}
int main()
{
  freopen("int","r",stdin);
  freopen("outc","w",stdout);
	int T,t;
	cin>>T;
	for (t=1;t<=T;t++)
	{
     int i,j,k,l,x,n;
     cin>>l>>x;
     n=l*x;
     string st;
     cin>>st;
     vector<int>v(l*x);
     for(i=0;i<l*x;i++)
     {
        j=i%l;
        v[i]=tell(st[j]);
     }
      int num=1;
      vector<int>ar(l*x,0);
      ar[l*x-1]=v[l*x-1];
      for(i=l*x-2;i>=0;i--)
      {
        ar[i]= mul(v[i],ar[i+1]);
      }
     // for(i=0;i<n;i++)
       // cout<<ar[i]<<" ";
     for(i=0;i<n-2;i++)
     {
        num=mul(num,v[i]);
        if(num==2)
        {
          int tem=1;
          for(j=i+1;j<n-1;j++)
          {
              tem=mul(tem,v[j]);
              if(tem==3 && ar[j+1]==4)
              {
                break;
              }
          }
          if(j<n-1)break;
        }
     }
     if(i<n-2)
     printf("Case #%d: YES\n",t);
     else
      printf("Case #%d: NO\n",t);
	}
  //Case #1: 0	
	return 0;
}