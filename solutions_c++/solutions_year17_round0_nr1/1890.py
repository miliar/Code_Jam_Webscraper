#include<bits/stdc++.h>
#define PI acos(-1)
#define ll long long
#define eps 1e-9
#define PB push_back
#define EB emplace_back
#define F first
#define S second
#define MP make_pair
#define RS resize
#define BG begin
#define sf scanf
#define pf printf
#define optimize() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define harmonic(n) 0.57721566490153286l+log(n)
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define MOD 1000000007
#define fraction() cout.unsetf(ios::floatfield); cout.precision(6); cout.setf(ios::fixed,ios::floatfield);
#define inf INT_MAX

using namespace std;

typedef vector<ll>   vli;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
typedef pair<ll,ll>   pll;
typedef vector<pii>  vpi;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef vector<pll> vpl;
typedef vector<vector<ll> > vvli;


int dx[] = {+1 , -1 , 0 , 0};
int dy[] = {0 , 0 , +1 , -1};
int dx2[] = {+1 , -1 , 0 , 0 , +1 , +1 , -1 , -1};
int dy2[] = {0 , 0 , +1 , -1 , +1 , -1 , -1 , +1};

ll squ(ll x)
{
    return (x*x);
}

ll power(ll bs,ll k)
{
    ll x = 1,y = bs;
    if(k == 0) return 1;

    while(k > 0){
        if(k % 2 == 1) x = (x * y) ;

        y *= y;
        k /= 2;
    }
    return x;
}

#define MX 1010

char change(char c)
{
    if(c == '+') return '-';
    else return '+';
}

int main()
{
    //optimize();
    fraction();

    int k,n,i,j,ans,tst,cs = 0;

    FILE *in,*out;

    char s[MX];
    in = fopen("panCakesmaL.txt","r");
    out = fopen("oppanCakesmL.txt","w");

    fscanf(in,"%d",&tst);

    while(++cs <= tst){
        fscanf(in,"%s %d",s,&k);
        n = strlen(s);
        ans = 0;
        for(i = 0 ;i <= n - k; i++){
            if(s[i] == '-'){
                for(j = i; j < i + k; j++){
                    s[j] = change(s[j]);
                }
                //printf("%s\n",s);
                ans++;
            }


        }

        for(i = n - k; i < n; i++){
            if(s[i] == '-'){
                fprintf(out,"Case #%d: IMPOSSIBLE\n",cs);
                break;
            }
        }

        if(i == n){
            fprintf(out,"Case #%d: %d\n",cs,ans);
        }
    }


    return 0;
}
