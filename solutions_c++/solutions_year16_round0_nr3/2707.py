#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

using namespace std;
typedef long long ll;

const int M = 10000000;

bool ee[M + 1];
vector<ll> prm;

ll isPrime(ll n){
    for(int j = 0;j < prm.size() && prm[j] * prm[j] <= n;j++)
        if(n % prm[j] == 0)
            return prm[j];
    int k = prm.size() - 1;
    if(prm[k] * prm[k] < n)
        for(ll i = prm[k];i * i <= n;i += 2)
            if(n % i == 0)
                return i;
    return 0;
}

void genPrm(ll lim){
    for(int i = 2;i <= M;i++)
    {
        if(ee[i]) continue;
        prm.pb(i);
        for(int j = i + i;j <= M;j += i)
            ee[j] = true;
    }
    
    for(ll i = M + 1;i <= lim;i++)
    {
        bool ok = true;
        for(int j = 0;j < prm.size() && prm[j] * prm[j] <= i;j++)
            if(i % prm[j] == 0){
                ok = false;
                break;
            }
        if(ok)
            prm.pb(i);
    }
}

ll checkInBase(ll n,ll base){
    ll val = 0;
    ll b = 1;
    FOR(i,16){
        val += ((n >> i) & 1LL) * b;
        b = b * base;
    }
    return isPrime(val);
}   

ll tmp[11];
int main(){
   // cout<<"Generate primes...\n";
    genPrm(M);
   // cout<<"Done!\n";
    
    int Cnt = 0;
    for(int m = 1 | (1 << 15);m < (1 << 16) && Cnt < 50;m += 2){
        bool ok = true;
        for(int b = 2;b <= 10;b++)
        {
            ll dv = checkInBase(m,b);
            if(dv == 0){ ok = false; break; }
            tmp[b] = dv;
        }
        if(ok){
            ++Cnt;
           // cout<<"PRIME "<<++Cnt<<"\n";
            for(int i = 15;i >= 0;i--)
                cout<<((m >> i) & 1);
            for(int i = 2;i <= 10;i++)
                cout<<" "<<tmp[i];
            cout<<"\n";
        }
    }
    
	return 0;
}
