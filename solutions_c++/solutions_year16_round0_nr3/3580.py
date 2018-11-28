#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <string.h>
#include <time.h>
#include <stack>
#include <set>
#include <queue>
#include <vector>
#include <list>
#define pb push_back
#define ll long long
#define mp make_pair
#define pll pair<long,long>
#define plll pair<long,long>
#define F first
#define S second
#define INF 1000000000


using namespace std;

ll a=0,b=0,c=0,d=1,BASE = 10000000000;
ll la=0,lb=0,lc=0,ld=0;

void multi(ll m){
    ll carry = 0;
    d *= m;
    carry = d / BASE;
    d %= BASE;
    c = (c*m)+carry;
    carry = c / BASE;
    c%= BASE;
    b = (b * m) + carry;
    carry = b / BASE;
    b %= BASE;
    a = (a * m) + carry;
}

bool diviser(ll m){
    ll ax=la,bx=lb,cx=lc,dx=ld;
    ax %= m;
    bx += ax * BASE;
    bx %= m;
    cx += bx * BASE;
    cx %= BASE;
    dx += cx * BASE;
    dx %= m;
    if(dx==0)
    return(true); else return(false);
}

void reset(){
    a=0,b=0,c=0,d=1;
}

void add(){
    ll carry=0;
    ld+=d;
    carry = ld/BASE;
    ld%=BASE;
    lc+=c+carry;
    carry = lc/BASE;
    lc%=BASE;
    lb+=b+carry;
    carry = lb/BASE;
    lb%=BASE;
    la+=a+carry;
}

void go(string s,ll c){
    for(int i=s.length()-1;i>=0;i--){
        if(s[i]=='1') add();
        multi(c);
    }
}

string toBin(ll a){
    string res="";
    while(a>0){
        if(a%2==0) res="0"+res; else res="1"+res;
        a/=2;
    }
    return(res);
}

int main()
{
    #ifdef LOCAL
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin.sync_with_stdio(0);
    cin.tie(0);
    cout<<"Case #1:"<<endl;
    long len = 16, cnt = 50;
    vector<int> ans;
    ll mask = ((ll)1<<(len-1))+(ll)1;
    ll i=0;
    while(cnt>0){
        ans.clear();
        for(int j=2;j<=10;j++){
            go(toBin(mask+(ll)i),j);
            for(int div = 2; div<1000;div++){
                if(la==0&&lb==0&&lc==0&&ld==div) break;
                if(diviser(div)) {ans.pb(div); break;}
            }
            //printf("%010lld%010lld%010lld%010lld\n",la,lb,lc,ld);
            la=lb=lc=ld=0;
            reset();
        }
        if(ans.size()==9){
            cout<<toBin(mask+(ll)i)<<' ';
            for(int f=0;f<ans.size();f++){
            cout<<ans[f]<<' ';}
            cout<<endl;
            cnt--;
        }
        i+=2;
        //cout<<toBin(mask+i)<<endl;
    }
    return 0;
}
