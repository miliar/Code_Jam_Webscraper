#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define FOR(i,ini,fin) for(int i=(int)ini;i<(int)fin;i++)
#define FOR_INC(i,ini,fin,inc) for(int i=(int)ini;i<(int)fin;i+=inc)
#define FOR_IT(iter,C) for(typeof(C.begin()) iter = C.begin();iter!=C.end();iter++)
#define all(A) A.begin(), A.end()
#define mem(x,val) memset(x,val,sizeof(x))
#define EPS 1e-7
#define MAY 10000002
#define INF 100000000
#define MOD 1000000007
#define PI 3.141592654
typedef long long LL;
typedef double D;
#define G(x) (D)(x)
#define F(x) (LL)(x)

int x[MAY];

int pal(LL n){
    if(n<0)assert(0);
    LL aux=n, inv=0;
    while(aux>0){
        inv=inv*10+aux%10;
        aux/=10;
    }
    return n==inv;
}
int main(){
/*
    int y=1000000;
    LL aux=1LL*y*y*y;
    cout<<aux<<" "<<1LL*y*y*y<<endl;
    int sq=(int)sqrt(aux);
    cout<<sq<<" "<<aux<<endl;
    */
    mem(x,0);
    FOR(i,1,MAY){
        if(pal(i)&&pal(1LL*i*i))x[i]=1;
        x[i]+=x[i-1];
    }
    //puts("ok");
    int T;
    LL a,b, inf,sup;
    cin>>T;
    FOR(t,1,T+1){
        cin>>a>>b;
        inf=1LL*sqrt(a), sup=1LL*sqrt(b);
        while(1LL*inf*inf<1LL*a)inf++;
        while(1LL*sup*sup>1LL*b)sup--;
        //cout<<inf<<" "<<sup<<endl;
        printf("Case #%d: ",t);
        if(inf>sup)cout<<0<<endl;
        else cout<<x[sup]-x[inf-1]<<endl;
    }

    return 0;
}

