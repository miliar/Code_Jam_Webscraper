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

int main()
{   
    ll t;
    cin>>t;
    for(int p=1;p<=t;p++){
        ll k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<p<<": ";
        for(int i=1;i<s;i++){
            cout<<i<<' ';
        }
        cout<<s<<endl;
    }

    
    //cout<<fixed<<setprecision(16)<<ans<<endl;
    return 0;
}













    