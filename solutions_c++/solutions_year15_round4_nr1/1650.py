#include<bits/stdc++.h>
#define set(p) memset(p,-1,sizeof(p))
#define clr(p) memset(p,0,sizeof(p))
#define ll long long int
#define llu unsigned long long int
#define si(n)					scanf("%d",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n)                                   scanf("%s",n)
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


long long int power(long long int x,long long int y)
{
    long long int temp,ty,my;
    long long int mod;
    mod=1000000007;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
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



long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}



string s[110];


int main()
{
    freopen("C:\\Users\\ABHISHEK004\\Desktop\\a11.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK004\\Desktop\\ab.out","w",stdout);
    int tt;
    cin>>tt;
    int R,i,C,j,k,kk;
    for (kk = 1; kk <= tt; kk++)
    {
        cin>>R>>C;
        for(i = 0; i < R; i++)
             cin>>s[i];

        bool check = true;

        int res = 0;

        for (i = 0; i < R; i++)
        for (j = 0; j < C; j++)
        if (s[i][j] != '.')
        {
            bool u = false;
            bool d = false;
            bool l = false;
            bool r = false;
            for (k = i - 1; k >= 0; k--)
                 if (s[k][j] != '.')
                    u = true;

            for (k = i + 1; k < R; k++)
                if (s[k][j] != '.')
                    d = true;

            for (k = j - 1; k >= 0; k--)
                if (s[i][k] != '.')
                    l = true;

            for (k = j + 1; k < C; k++)
                if (s[i][k] != '.')
                    r = true;

            if (u == false && d == false && l == false && r == false)
                check = false;
            else
                {
                    bool is = false;

                    if (s[i][j] == '>' && r )
                        is = true;
                    if (s[i][j] == '<' && l )
                        is = true;
                    if (s[i][j] == 'v' && d )
                        is = true;
                    if (s[i][j] == '^' && u )
                        is = true;
                    if (is == false)
                    res++;
                }
        }
        if (check == false)
        cout<<"Case #"<<kk<<": "<<"IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<kk<<": "<<res<<endl;
    }

    return 0;
}
