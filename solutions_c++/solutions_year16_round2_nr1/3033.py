#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007

ll power(ll base,ll exp){
    ll res = 1;
    while(exp){
        if(exp&1) res = (res*base)%mod;
        base = (base*base)%mod;
        exp>>=1;
    }
    return res;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll T;
    scanf("%lld",&T);
    ll num = T;
    while(T--){
        ll x;
        ll a[260]={0};
        string str;
        cin>>str;
        ll n = str.length();
        for(ll i=0;i<n;i++){
            a[str[i]]++;
        }
        ll j=0;
        ll ARR[10000];
        if(a['Z']>=1){
            ll s = j;
            for(ll i=j;i<s+a['Z'];i++,j++)
            ARR[j] = 0;
            ll s1 = a['Z'];
            a['Z'] -= s1;
            a['E'] -= s1;
            a['R'] -= s1;
            a['O'] -= s1;
        }
        if(a['U']>=1){
             ll s = j;
            for(ll i=j;i<s+a['U'];i++,j++)
            ARR[j] = 4;
            ll s1 = a['U'];
            a['U'] -= s1;
            a['F'] -=  s1;
            a['R'] -= s1;
            a['O'] -=  s1;


        }
         if(a['X']>=1){
             ll s = j;
             for(ll i=j;i<s+a['X'];i++,j++)
            ARR[j] = 6;
            ll s1 = a['X'];
            a['X'] -= s1;
            a['S'] -=  s1;
            a['I'] -=  s1;


        }
        if(a['G']>=1){
            ll s = j;
            for(ll i=j;i<s+a['G'];i++,j++)
            ARR[j] = 8;
             ll s1 = a['G'];
            a['G'] -= s1;
            a['E'] -= s1;
            a['I'] -=  s1;
            a['H'] -=  s1;
            a['T'] -=  s1;


        }
        if(a['W']>=1){
             ll s = j;
            for(ll i=j;i<s+a['W'];i++,j++)
            ARR[j] = 2;
             ll s1 = a['W'];
            a['W'] -= s1;
            a['T'] -=s1;
            a['O'] -=s1;

        }
        if(a['O']>=1){
               ll s = j;
            for(ll i=j;i<s+a['O'];i++,j++)
            ARR[j] = 1;
                ll s1 = a['O'];
            a['O'] -= s1;
            a['N'] -= s1;
            a['E'] -=s1;

        }
        if(a['F']>=1){
               ll s = j;
            for(ll i=j;i<s+a['F'];i++,j++)
            ARR[j] = 5;
                ll s1 = a['F'];
            a['F'] -= s1;
            a['I'] -= s1;
            a['V'] -= s1;
            a['E'] -= s1;

        }
        if(a['V']>=1){
             ll s = j;
            for(ll i=j;i<s+a['V'];i++,j++)
            ARR[j] = 7;
                ll s1 = a['V'];
            a['S'] -=s1;
            a['E'] -=s1;
            a['v'] -= s1;
            a['E'] -= s1;
            a['N'] -= s1;

        }
        if(a['I']>=1){
              ll s = j;
            for(ll i=j;i<s+a['I'];i++,j++)
           ARR[j] = 9;
               ll s1 = a['I'];
            a['N'] -= 2*s1;
            a['E'] -= s1;
            a['I'] -= s1;

        }
        if(a['T']>=1){
             ll s = j;
            for(ll i=j;i<s+a['T'];i++,j++)
           ARR[j] = 3;
        }
        printf("Case #%lld: ",num-T);
        sort(ARR,ARR+j);
        for(ll i=0;i<j;i++)
        printf("%lld",ARR[i]);
        printf("\n");
    }
    return 0;
}
