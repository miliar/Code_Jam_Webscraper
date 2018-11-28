#include<bits/stdc++.h>
using namespace std;
#define M 100005
#define lo long long
bool vis[10];
int get_dig(lo n)
{
   while(n>0)
   {
     vis[n%10]=true;
     n/=10;
   }
   int ans=0;
   for(int i=0;i<10;i++)
   {
     if(vis[i]==true)
      ans++;
   }
   return ans;
}
int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  int p;
  p=0;
  while(t--)
  {
    p++;

    lo n;
    cin>>n;
    cout<<"Case #"<<p<<": ";
    if(n==0)
    {
      cout<<"INSOMNIA"<<endl;
      continue;
    }
    memset(vis,0,sizeof(bool)*10);
    int cnt;
    for(lo i=1;;i++)
    {
      cnt=get_dig(n*i);
      if(cnt==10)
      {
        cout<<(n*i)<<endl;
        break;
      }
    }
  }
  return 0;
}

