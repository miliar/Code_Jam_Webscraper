#include <bits/stdc++.h>

#define set(p) memset(p,-1,sizeof(p))
#define clr(p) memset(p,0,sizeof(p))
#define ll long long int
#define llu unsigned long long int
#define si(a) scanf("%d",&a)
#define rep(i,a,n) for(i=(a);i<(n);i++)
#define pii pair<int,int>
#define pb(x) push_back(x)
#define v(x) vector<x>

using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


long long int power(long long int x,long long int y,ll mod)
{
    long long int temp,ty,my;

    if( y == 0)
        return 1;
    temp = power(x, y/2,mod);
    ty=(temp%mod)*(temp%mod);
    if (y%2 == 0)
        {

                return ty%mod;
        }
    else
        {
                my=(x%mod)*(ty%mod);
                return my%mod;
        }
}



long long int maxxi(long long int a,long long int b)
{
        return a>b?a:b;
}

long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}




struct abhi
{
       ll val;
       ll arr1;
};

struct abhi brr[100010];

bool cmp(struct abhi x,struct abhi y)
{
        return x.arr1<y.arr1;
}



int main()
{
     freopen("C:\\Users\\ABHISHEK004\\Desktop\\aa.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK004\\Desktop\\ab.out","w",stdout);
    int t,n,i,tot,soln,j;
    si(t);

    int tt=t;
    while(t--)
    {
        string s;
        cin>>n;
        cin>>s;
        tot = 0;
        soln = 0;
        rep(i,0,n+1)
        {
            if((s[i]-48)>=0)
            {
                if(tot<i)
                {
                    soln = soln + (i - tot);
                    tot = tot + (i - tot);
                }
            }
            tot = tot + s[i] - 48;
        }
        cout<<"Case #"<<tt-t<<": "<<soln<<"\n";
    }

    return 0;
}


