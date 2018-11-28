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
int p[100], now[5];
int main(){
    int t,r,n,m,k;
    cin>>t;
    cin>>r>>n>>m>>k;
    puts("Case #1:");
    FOR(cases,0,r){
        FOR(i,0,k)cin>>p[i];
        vector<int>res;
        FOR(x,2,m+1)FOR(y,2,m+1)FOR(z,2,m+1){
            if(res.size())break;
            now[0]=x, now[1]=y, now[2]=z;
            set<int>have;
            FOR(mask,0,(1<<3)){
                int num=1;
                FOR(a,0,3)if(mask&(1<<a))num*=now[a];
                have.insert(num);
            }
            int yes=1;
            FOR(i,0,k)if(!have.count(p[i]))yes=0;
            if(yes)res.pb(x), res.pb(y), res.pb(z);
        }
        if(res.size()>0){
            //puts("!yes");
            cout<<res[0]<<res[1]<<res[2]<<endl;
        }
        else puts("222");
    }
    return 0;
}
