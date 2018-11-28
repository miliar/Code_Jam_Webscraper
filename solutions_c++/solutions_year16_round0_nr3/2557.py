#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <fstream>
#define mod 1000000007
#define size 1000007
#define ll long long
#define INF LLONG_MAX
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;

int str[100];
int cunt,n,j;

bool isPrime(ll val){
    for(ll i=2;i<=sqrt(val);i++)
        if(val%i==0)
            return false;
    return true;
}

ll divisor(ll val){
    for(ll i=2;i<=sqrt(val);i++)
        if(val%i==0)
            return i;
}

void print(){
    int i,base;
    ll ans,val;
    for(i=0;i<n;i++) cout<<str[i];
    cout<<" ";
    for(base=2;base<=10;base++){
        ans = 0;val = 1;
        for(i=n-1;i>=0;i--,val*=base)
            ans+=val*str[i];
        cout<<divisor(ans)<<" ";
    }
    cout<<"\n";
}

void check(){
    ll ans,val;
    int base,i;
    for(base=2;base<=10;base++){
        ans = 0;val = 1;
        for(i=n-1;i>=0;i--,val*=base)
            ans+=val*str[i];
        if(isPrime(ans))
            return;
    }
    cunt++;
    print();
}

void permute(int i){
    if(i==n-1){
        check();
        if(cunt==j)
            exit(0);
        return;
    }
    str[i] = 0;
    permute(i+1);
    str[i] = 1;
    permute(i+1);
}

int main() {
    //freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
    //ios::sync_with_stdio(0);
    int tc;
    cin>>tc>>n>>j;
    cout<<"Case #1: \n";
    cunt = 0;
    str[0] = str[n-1] = 1;
	permute(1);
	return 0;
}
