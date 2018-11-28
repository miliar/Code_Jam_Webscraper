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
    ll n,t;
    cin>>t;

    for(int i=1;i<=t;i++){
        cin>>n;
        cout<<"Case #"<<i<<": ";
        int j=1;
        vector<char> b(10,0);
        while(j<10000 && check(b,n*j)<10){
            j++;
        }
        if(j!=10000){
            cout<<n*j<<endl;
        }else{
            cout<<"INSOMNIA"<<endl;
        }
    }

    
    //cout<<fixed<<setprecision(16)<<ans<<endl;
    return 0;
}













    