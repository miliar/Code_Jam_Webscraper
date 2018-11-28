//Шаблон

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <utility>

#define ll long long
#define MAXN 200100

using namespace std;

struct point
{
    ll x;
    ll y;
    point(ll a=0, ll b=0){
        x=a;
        y=b;
    }
};

double sqr(double a){return a*a;}

bool cmpx(point a, point b){
    return (a.x<b.x)||((a.x==b.x)&&(a.y<b.y));
}

int check(vector<char>& a, ll n){
    do{
        a[n%10]=1;
        n/=10;
    }while(n);
    int res=0;
    for(int i=0;i<10;i++)res+=a[i];
    return res;
}

vector<ll> prime(1);
vector<bool> b(100000000);
vector<vector<ll> > d(11, vector<ll> (17,1));

ll get_numb(int mask, int i){

    ll res=0;
    for(ll j=0;j<15;j++){
        res+=d[i][j]*((mask >> j)&1);
    }
    return res+d[i][15];
}

ll is_prime(ll p){
    for(int i=0;i<prime.size();i++){
        if(p%prime[i]==0){
            return prime[i];
        }
    }
    return p;
}
ll ans[11];

int main()
{   
    prime[0]=2;
    for(int i=3;i<=100000000;i++){
        if((i&1)&& !b[i]){
            prime.push_back(i);
            ll l=i;
            l*=l;
            while(l<=100000000){
               b[l]=true; 
               l+=i; 
            }
        }
    }
    for(ll i=2;i<=10;i++){
        for(ll j=1;j<=16;j++){
            d[i][j]=d[i][j-1]*i;
        }
    }
    //return 0;
    cout<<"Case #1: "<<endl;
    int k=0;
    for(int mask=1;mask<(1ll<<15);mask+=2){
        bool bb=true;
        for(int i=2;i<=10;i++){
            ll x=get_numb(mask,i);
            ll del=is_prime(x);
            if(del==x){
                bb=false;
                break;
            }
            ans[i]=del;
        }
        if(bb){
            cout<<1;
            for(int j=14;j>=0;j--)
                cout<< ((mask>>j)&1);
            for(int i=2;i<=10;i++)
                cout<<' '<<ans[i];
            cout<<endl;
            k++;
        }
        if(k==50){
            break;
        }
    }

    
    //cout<<fixed<<setprecision(16)<<ans<<endl;
    return 0;
}













    