
/************** Elvis Rusnel Capia Quispe ***************/
#include <bits/stdc++.h>
#define f(i,x,y) for (int i = (x); i < (y); i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define MOD 1000000007
#define INF 1000000000
#define HASH unsigned long long
#define bug1(x) cout<<#x<<" = "<<x<<endl
#define bug2(x,y) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<endl
#define bug3(x,y,z) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<endl
#define bug4(x,y,z,m) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<" "<<#m<<" = "<<m<<endl
#define sc(x) scanf("%d",&x)
#define ana(x) cout<<"NO JUST FOR ME"<<endl
#define MAXN 100005

using namespace std;
ll alice,num[105];

ll a_exp_b(ll a,ll b)
{   ll ans = 1;
    while(b)
    {   if(b&1) ans = ans * a;
        a = a * a;
        b/=2;
    }
return ans;
}

ll rec(ll cant,int pos,int lim)
{   if(lim==pos) return 0;

    ll ans = 0;
    if(cant > num[pos] )
    ans = rec(cant + num[pos],pos + 1,lim);
    else
    {   if(cant==1) return INF;
        ll k = log2( (1.0*num[pos] - 1.0)/(1.0*cant - 1.0)) + 1;

    ans = k +  rec(cant + num[pos] + (a_exp_b(2,k) - 1)*(cant-1),pos + 1,lim);
    }
return ans;
}

int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);
   int n , tc , nc = 1;
   sc(tc);

   while(tc--)
   {    cin>>alice>>n;
        f(i,0,n)
        cin>>num[i];

        sort(num,num+n);

        ll ans = n;

        f(i,0,n+1) // i es el final
        {   ll aux = rec(alice,0,i);
            ans = min(ans, n - i + aux);
            //veamos hasta cuadno
        }
    printf("Case #%d: %lld",nc++,ans);
    puts("");
   }

    return 0;
}

