#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstdarg>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

#if __cplusplus > 199711L
    void read(){}
    template<typename... T>
    void read(int& head, T&... tail) {scanf("%d",&head); read(tail...);}

    #define DB(args...) { cerr << __LINE__<< ": "; vector<string> _v = split(#args, ','); err(_v.begin(), args); }
    vector<string> split(const string& s, char c) {
        vector<string> v;stringstream ss(s);string x;
        while (getline(ss, x, c)) v.push_back(x);
        return move(v);
    }
    void err(vector<string>::iterator it) {cerr<<endl;}
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << "  "; err(++it, args...);
    }
#else
    #define DB(e) cerr << __LINE__ << ": " << #e << " = " << e << endl;
    void read(int& head) {scanf("%d",&head);}
#endif

#define ll long long int
#define pb push_back
#define fr(i,n)     for(int i=0;i<n;i++)
#define init(mem,v) memset(mem,v,sizeof(mem))
typedef pair<int,int> pii;

/* RABIN MILLER TEST */

ll mul(ll a,ll b,ll c){
    ll x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}

ll mod(ll a,ll b,ll c){
    ll x=1,y=a;
    while(b > 0){
        if(b%2 == 1){
            x=mul(x,y,c);
        }
        y = mul(y,y,c);
        b /= 2;
    }
    return x%c;
}

bool miller(ll p,ll it){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }

    ll s=p-1;
    while(s%2==0){
        s/=2;
    }

    for(ll i=0;i<it;i++){
        ll a=rand()%(p-1)+1;
        ll tt=s;
        ll md=mod(a,tt,p);

        while(tt!=p-1 && md!=1 && md!=p-1){
            md=mul(md,md,p);
            tt *= 2;
        }
        if(md!=p-1 && tt%2==0){
            return false;
        }
    }
    return true;
}

#define PRE_LIM 10000000
bool prime[PRE_LIM];
int divs[PRE_LIM];

void init_mem(){
    for(int i=0;i<PRE_LIM;i++){
        prime[i]=true;
    }
    prime[0]=false;
    prime[1]=false;
    for(int i=2;i<PRE_LIM;i++){
        if(prime[i]){
            int f=2*i;
            while(f<PRE_LIM){
                prime[f]=false;
                divs[f]=i;
                f+=i;
            }
        }
    }
}

bool cprime(ll n){
    if(n<PRE_LIM) return prime[n];
    else return miller(n,1);
}

#define mx 16

ll proof[10];

#define limit 1000
bool can_find_easy_proof(ll n, ll& pos){
    fr(i,limit) if(prime[i] and n%i==0){
        pos=i;
        return true;
    }
    return false;
}

bool test(int mask){
    for(int base=2;base<=10;base++){
        ll n=0;
        int tmp=mask;

        while(tmp){
            n=base*n+(tmp&1);
            tmp>>=1;
        }

        if(cprime(n)) return false;
        if(!can_find_easy_proof(n, proof[base])) return false;
    }
    return true;
}

void print(int mask){
    while(mask){
        printf("%d",mask&1);
        mask>>=1;
    }
    printf(" ");
    for(int base=2;base<=10;base++){
        printf("%lld ",proof[base]);
    }
    printf("\n");
}

int main(){
    init_mem();

    int j=50;
    for(int maskpart=0;maskpart<(1<<mx-2);maskpart++){
        int mask=(1<<(mx-1)) + (maskpart<<1) + 1;

        if(test(mask)){
            print(mask);
            j--;
            if(j==0) break;
        }
    }
}
