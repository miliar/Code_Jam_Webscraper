#include <cstdio>
#define ll long long

int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
//freopen("out.txt","w",stdout);
  int t;
  scanf("%d",&t);
  for(int x=1;x<=t;x++)
  {
    ll n,ans=0;
    scanf("%lld",&n);
    int mark[10];
    for(int i=0;i<10;i++)
      mark[i]=0;
    for(int i=1;i<100;i++)
    {
      ll a = n*i;
      ll s = a;
      while(a)
      {
        mark[a%10]=1;
       // printf("a %lld mark %d\n",a%10,mark[a%10]);
        a/=10;
      }
      bool f = false;
      for(int j=0;j<10;j++)
        if(!mark[j])
          {f=true;break;}
        if(!f)
        {ans=s;break;}
    }
    if(!ans)
      printf("Case #%d: INSOMNIA\n",x);
    else
      printf("Case #%d: %lld\n",x,ans);

  }
 
    return 0;
}
 