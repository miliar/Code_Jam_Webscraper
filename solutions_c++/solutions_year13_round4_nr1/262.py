#include<cstdio>
#include<ctime>
#include<cmath>
#include<cctype>

#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<stack>
#include<queue>
using namespace std;
#define pb push_back
#define mp make_pair
#define FILEIN "A.in"
#define FILEOUT "A.txt"
const long long MOD=1000002013;
long long abs(long long N){
    if(N>=0)
        return N;
    return -N;
}
long long cnt(long long a, long long b,long long N){
    if(a==b)
        return 0;
    else{
        long long d = labs(a-b);
        return (N+1)*d-(d)*(d+1)/2;
    }
}
int main(){
    freopen(FILEIN,"r",stdin);
    freopen(FILEOUT,"w",stdout);
    int t;
    cin>>t;
    for(int u=1;u<=t;++u){
        int N,M;
        cin>>N>>M;
        vector<pair<long long,pair<long long,long long> > > ras;
        long long curpr=0;
        for(int i=0;i<M;++i){
            long long o,e,p;
            cin>>o>>e>>p;
            ras.pb(mp(o,mp(0,p)));
            ras.pb(mp(e,mp(1,p)));
            curpr=(curpr+(cnt(o,e,N)%MOD*p)%MOD)%MOD;
        }
        //cout<<curpr<<endl;
        sort(ras.begin(),ras.end());
        stack<pair<long,long> > q;
        long long sumpr=0;
        for(int i=0;i<ras.size();++i){
            if(ras[i].second.first==0)
                q.push(mp(ras[i].first,ras[i].second.second));
            else{
                int curp=ras[i].second.second;
                int curv=0;
                pair<long long,long long> cur;
                while(curv<curp){
                    if(curv==curp)
                        break;
                    cur=q.top();
                    q.pop();
                    if(curv+cur.second<=curp){
                        sumpr=(sumpr+(cnt(cur.first,ras[i].first,N)%MOD*cur.second%MOD))%MOD;

                        curv+=cur.second;
                    }
                    else{
                        sumpr=(sumpr+(cnt(cur.first,ras[i].first,N)%MOD*(curp-curv)%MOD))%MOD;
                        q.push(mp(cur.first,cur.second-(curp-curv)));
                        curp=curv;
                    }

                }
            }
        }
        cout<<"Case #"<<u<<": ";
        cout<<(curpr+MOD-sumpr)%MOD<<endl;

    }
    return 0;
}
