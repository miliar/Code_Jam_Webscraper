#include<iostream>
#include<cmath>
using namespace std;

typedef long long ll;

int chk_palin(int n)
{
    int a = n,rev=0;
    
    while(n>0)
    {
              int t = n%10;
              rev = rev*10 + t;
              n /= 10;
    }
    
    if(rev==a)
              return 1;
    else return 0;
}

int main()
{
    
    freopen("C-small-attempt2.in","r",stdin);
    freopen("out.out","w",stdout);
    
    
    int t,x=1;
    scanf("%d\n",&t);
    
    while(t--)
    {
              ll a,b;
              scanf("%lld %lld\n",&a,&b);
              
              int cnt=0;
              
              ll sqa=(ll)sqrt(a);
              ll sqb=(ll)sqrt(b);
              
              if(chk_palin(sqa) && sqa*sqa>=a && chk_palin(sqa*sqa))
                            cnt++;
                            
              for(ll k=sqa+1;k<=sqb;k++)
              {
                    if(chk_palin(k) && chk_palin(k*k))
                    {
                             //       cout<<k*k<<endl;
                                               cnt++;
              }}
              
              printf("Case #%d: %d\n",x++,cnt);
    }
}                     
