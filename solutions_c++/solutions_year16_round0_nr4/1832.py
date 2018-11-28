#include <bits/stdc++.h>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <deque>
#include "prettyprint.h"
#include <deque>
#include <fstream>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define M_PI 3.14159265358979323846
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define LD long double
#define INF 1000000000
#define int long long
/*bool sieve[1000005];
set<int> primes;
bool isPrime(int i){
    if(i < 1000005){
        return !sieve[i];
    } else{
        int temp = sqrtl(i);
        for(int prime: primes){
            if( !(i % prime)){
                return false;
            }
            if(prime > temp){
                return false;
            }
        }
        return true;
    }
}

//Begin of the code
#undef int
int main() {
#define int long long
    int x = 2;
    for(int x = 2; x < 1000005; x++){
        if(sieve[x]) continue;
        primes.insert(x);
        for(int k = 2 * x; k < 1000005; k += x){
            sieve[k] = true;
        }
    }
    int n = 6;
    int c = 3;
    int m = powl(2, n - 2);
    vector<pair<int,vector<pair<int,int>>>> res;
    for(int i = 0; i < m && res.size() != c; i++){
        //cout<<res<<endl;
        vector<int> a(11,0);
        for(int k = 2; k <= 10; k++){
            a[k] += 1;
            a[k] += powl(k, n - 1);
        }
        int pot = 1;
        int tempi = i;
        while(tempi){
            int bit = tempi & 1;
            tempi /= 2;
            for(int k = 2; k <= 10; k++){
                a[k] += bit * powl(k, pot);
            }
            pot++;
        }
        vector<pair<int,int>> mRes;
        for(int k = 2; k <= 10; k++){
            if(isPrime(a[k])){
                goto end;
            } else{
                for(int prime: primes){
                    if( !(a[k] % prime)){
                        mRes.PB(MP(a[k],prime));
                        break;
                    }
                }
            }
        }
        res.PB(MP(a[10], mRes));
        end:
        continue;
    }
    cout<<"Case #1: \n";
    REP(i, res.size()){
        cout<<res[i].ST<<" ";
        for(pair<int,int> j: res[i].ND){
            cout<<j<<" ";
        }
        cout<<"\n";
    }

    return 0;
}*/
#undef int
int main(){
#define int long long
    int t;
    cin>>t;
    REP(q,t){
        cout<<"Case #"<<q + 1<<": ";
        int k,c,s;
        cin>>k>>c>>s;
        REP(i, s){
            cout<<i + 1<<" ";
        }
        cout<<endl;
    }

    return 0;
}
