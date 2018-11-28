#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll nn,jj;
ll c;

ll divisor(ll n){
    for(int i=2;i<n;i++){
        if(!(n%i))
            return i;
    }
}

ll convert(string s,ll b){
    ll i,j,n = s.length();
    ll sum=0; j = 1;
    for(i=n-1;i>=0;i--){
        sum+= j*(s[i]-48);
        j = j*b;
    }
    return sum;
}

bool isprime(ll N){
    ll i;
    if(N<2 || (!(N&1) && N!=2))
        return false;
    for(i=3; i*i<=N; i+=2){
        if(!(N%i))
            return false;
    }
    return true;
}

bool solve(string s,ll b){
    ll i,j,n = s.length();
    ll sum = 0; j = 1;
    for(i=n-1;i>=0;i--){
        sum+= j*(s[i]-48);
        j = j*b;
    }
    if(isprime(sum))
        return false;
    return true;
}

void bin(ll n)
{
    ll i; string s = "";
    for(i=1<<(nn-1);i>0;i=i/2){
        if(n&i)
            s+= "1";
        else
            s+= "0";
    }
    ll p = s.length();
    if(s[0]=='0' || s[p-1]=='0')
        return;
    ll flag=1;
    for(i=2;i<=10;i++){
        if(!solve(s,i)){
            flag=0; break;
        }
    }
    ll x,ans;
    if(flag){
        c++;
        cout << s << " ";
        for(i=2;i<=10;i++){
            x = convert(s,i);
            ans = divisor(x);
            printf("%lld ",ans);
        }
        printf("\n");
    }
}

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,j=1; scanf("%d",&t);
    while(t--){
        scanf("%lld%lld",&nn,&jj);
        ll i; ll s = pow(2,nn);
        c=0;
        printf("Case #%d:\n",j);
        for(i=2;i<=s;i++){
            if(c<jj)
                bin(i);
        }
        j++;
    }
    return 0;
}
