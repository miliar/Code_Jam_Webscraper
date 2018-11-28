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

int main(){
    int t;
    LL a, n,x;
    cin>>t;
    FOR(cas,1,t+1){
        cin>>a>>n;
        vector<int>v;
        FOR(i,0,n)cin>>x, v.pb(x);
        sort(all(v));
        while(v.size()>0 &&F(v[0])<F(a)){
            a=F(a)+F(v[0]);
            v.erase(v.begin());
        }
        n=v.size();
        int res=n;
        vector<int>w;
        FOR(i,0,n){
            w.pb(v[i]);
            int ope=n-w.size();
            LL now=F(a);
            vector<int>u=w;
            reverse(all(u));
            while(u.size()>0&&ope<res){
                assert(now>=0LL);
                if(F(now)>F(u.back())){
                    now=F(F(now)+F(u.back()));
                    u.erase(u.end()-1);
                }
                else if(now>1){
                    ope++, now=F(F(now)+F(F(now)-F(1)));
                }
                else {ope=10000000;break;}
            }
            res=min(res,ope);
        }
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
