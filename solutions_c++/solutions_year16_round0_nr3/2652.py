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

lli N = 16;
lli p[11][21];

bool prime(lli x){
    for(lli i=2;i*i<=x;i++){
        if(x%i == 0)
            return false;
    }
    return true;
}

lli anyfactor(lli x){
    for(lli i=2;;i++){
        if(x%i == 0)
            return i;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    debug = 1;
#endif
    srand (time(NULL));

    for(lli i=2;i<=10;i++){
        p[i][0] = 1;
        for(lli j=1;j<=20;j++)
            p[i][j] = p[i][j-1]*i;
    }
    cout<<"Case #1:\n";
    lli cnt = 0;
    for(lli mask=0;mask<(1<<(N-2));mask++){
        lli n = mask;
        n *= 2;
        n ++;
        n |= 1<<(N-1);
        bool fff = false;
        //for(lli j=N-1;j>=0;j--)cout<<bit(n,j);cout<<" ";
        for(lli i=2;i<=10;i++){
            lli temp = 0;
            for(lli j=0;j<N;j++){
                if(bit(n,j)){
                    temp += p[i][j];
                }
            }
            //cout<<temp<<","<<prime(temp)<<" ";
            fff |= prime(temp);
        }
        if(!fff){
            for(lli j=N-1;j>=0;j--)
                cout<<bit(n,j);
            cout<<" ";
            for(lli i=2;i<=10;i++){
                lli temp = 0;
                for(lli j=0;j<N;j++)
                    if(bit(n,j))
                        temp += p[i][j];
                cout<<anyfactor(temp)<<" ";
            }
            cout<<"\n";
            cnt++;
            if(cnt==50)
                break;
        }
    }

    return 0;
}

