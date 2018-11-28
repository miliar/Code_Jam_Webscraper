#include<bits/stdc++.h>

#define lli long long int
#define llu unsigned long long int
#define ld long double
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define slli(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);

const long double EPS = 1e-10;
const lli MOD = 1000000007ll;
const lli mod1 = 1000000009ll;
const lli mod2 = 1100000009ll;
int INF = 2147483645;
lli INFINF = 9223372036854775807;
int debug = 0;

using namespace std;

void print(int a[],int s,int e){for(int i=s;i<=e;i++)cout<<a[i]<<" ";cout<<"\n";}
void print(vector<int> &v,int s,int e){for(int i=s;i<=e;i++)cout<<v[i]<<" ";cout<<"\n";}
void print(vector<int> &v){for(int x:v)cout<<x<<" ";cout<<"\n";}

lli bit_count(lli _x){lli _ret=0;while(_x){if(_x%2==1)_ret++;_x/=2;}return _ret;}
lli bit(lli _mask,lli _i){return (_mask&(1<<_i))==0?0:1;}
lli powermod(lli _a,lli _b,lli _m){lli _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}
lli add(lli a,lli b,lli m=MOD){lli x=a+b;while(x>=m)x-=m;return x;}
lli sub(lli a,lli b,lli m=MOD){lli x=a-b;while(x<0)x+=m;return x;}
lli mul(lli a,lli b,lli m=MOD){lli x=a*b;x%=m;return x;}

int T,N;
int cnt[2000];
int mm = -1;
bool vis[10];

bool done(){
    for(int i=0;i<10;i++)
        if(!vis[i])
            return false;
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    debug = 1;
#endif
    srand (time(NULL));

    si(T);
    for(int t=1;t<=T;t++){
        si(N);
        if(N==0){
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        for(int i=0;i<10;i++)
            vis[i] = false;
        for(int i=1;;i++){
            int x = i*N;
            while(x){
                vis[x%10] = true;
                x /= 10;
            }
            if(done()){
                printf("Case #%d: %d\n",t,i*N);
                break;
            }
        }
    }

    return 0;
}

