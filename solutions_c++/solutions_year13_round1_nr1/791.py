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
#define MAY 1000005
#define INF 100000000
#define MOD 1000000007
#define PI 3.141592654
typedef long long LL;
#define F(x) (LL)(x)
typedef double D;
#define G(x) (D)(x)
int ok(LL x, D a0, D t){
    //cout<<"busco "<<x<<" rings y tengo "<<a0<<" t:"<<t<<endl;
    D an=D(D(a0)+D(4.0)*D(x-1));
    D sum=D(D(a0)+D(an));
    sum=D(D(sum)*D(x));
    sum=D(D(sum)/D(2.0));
    sum=D(sum);
    //cout<<"a0 "<<a0<<" a"<<x<<":"<<an<<" SUM ES "<<sum<<endl;
    if(sum>t)return 0;
    return 1;
}
int main(){
    int T;
    LL r,t;
    cin>>T;
    FOR(cas,0,T){
        cin>>r>>t;
        D a0=G(G(r+1)*G(r+1))-G(G(r)*G(r));
        LL res, inf=0, mid, sup=2000000000000000000LL;
        while(inf<=sup){
            mid=F((F(inf)+F(sup))/F(2));
            if(ok(mid, a0,D(t)))inf=mid+1, res=mid;
            else sup=mid-1;
        }
        printf("Case #%d: ",cas+1);
        cout<<res<<endl;
    }
    return 0;
}
