#include <iostream>
#include <cassert>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

typedef long long LL;
typedef vector<int> vi;

const int N=12;
const int A=27;
const LL mod=1000*1000*1000+7;
int n;
string a[N];

int have[N][A], pure[N], ed[N], bg[N], vis[A];
LL rec[A+2][1<<N];

LL dp(int last, int st, vector<int>vis){
    if(st==(1<<n)-1) return 1;
    LL &res=rec[last][st];
    if(res >=0) return res;
    res =0;
    for(int i=0; i<n; i++)
        if(!((1<<i)&st)){
            vi t=vis;
            bool suc=true;
            int cur=last;
            for(int j=0; suc&&j<a[i].size(); j++){
                int x=a[i][j]-'a';
                if(x != cur){
                    if(t[x]) suc=false;
                    t[x]=1;
                    cur = x;
                }
            }
            if(suc) res += dp(cur, st|(1<<i), t);
        }
    return res;
}

int main(int argc, const char * argv[])
{
    int ncase; cin>>ncase;
    for(int ca=1; ca<=ncase; ca++){
        cin>>n;
        memset(have, 0, sizeof(have));
        
        for(int i=0; i<n; i++)
            cin>>a[i];
        
        LL res=0;
        memset(rec, -1, sizeof(rec));
        vector<int> vis(A,0);
        cout<<"Case #"<<ca<<": "<<dp(26,0,vis)<<endl;
    }
    return 0;
}

