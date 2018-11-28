#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);
const int  MAX=100;
int N,J;
vector<string> possibleCoin;

ll anyBasetoDecimal ( string r,ll b) {
    ll p=1,res=0;
    for(int i=r.size()-1;i>=0;i--) {
        ll d=(r[i]<='9'? r[i]-'0' : r[i]-'A'+10);
        res+=d*p;
        p*=b;
    }
    return res;
}

string decimalToAnyBase(ll n,ll b) {
    string r="";
    while(n>0) {
        ll d=n%b;
        r+=((d<=9)?char(d +'0'):char(d-10+'A'));
        n/=b;
    }
    if(r.empty()) {
        r+='0';
    }
    reverse(r.begin(),r.end());
    return r;
}
bool prime(ll x) {
    for(ll i=2;i*i<=x;i++) {
        if(x%i==0) {
            return false;
        }
    }
    return true;
}


ll find(ll x) {
    for(ll i=2; i*i<=x;i++) {
        if(x%i==0) {
            return i;
        }
    }
}
int main()
{
	ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;
    cin>>N>>J;
    for(ll mask=(1ll<<(N-1))+1;mask<(1ll<<N);mask+=2) {
        if( (mask & (1ll<<0)) && (mask & (1ll<<(N-1))) ) {
            possibleCoin.push_back((decimalToAnyBase(mask,2)));
        } 
        //cout<<decimalToAnyBase(mask,2)<<"\n";
    }
    cout<<"Case #1:"<<"\n";
    for(string x : possibleCoin) {
        if(J<=0) {
            break;
        }
        bool ok=true;
        vector<ll> divisors(20);
        for(int base=2;base<=10;base++) {
            ll num=0;
            for(char d : x) {
                num*=base;
                num+=(d-'0');
            }
            if(prime(num)){
                ok=false;
                break;
            }
            divisors[base]=find(num);
        }
        if(ok) {
            cout<<x<<" ";
            for(int base=2;base<=10;base++) {
                cout<<divisors[base]<<" ";
            }
            cout<<"\n";
            J--;
        }
            
    }
	return 0;

}
