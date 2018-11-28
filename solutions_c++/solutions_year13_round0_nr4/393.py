/* Bismillahir Rahmanir Rahim */
/*Coder: Ahmad Faiyaz*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <fstream>

# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-11
#define inf 1234567891
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

# define VI vector<int>
# define VS vector<string>
# define VC vector<char>

#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define pii pair<int,int>
#define UNIQUE(c) (c).resize( unique( all(c) ) - (c).begin() )

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;

template <class stl>
void DBGSTL (stl a) { // for deque, vector , set
    FORIT(i,a){
        cerr<<*i<<" ";
    }
    cerr<<"\n";
    return;
}
int init [505];
int open [505];
vector <int> will [505];
int t,chk=1,K,N,x,op,k;
vector <int> first;
int lim;

map <int,int> find_it(int msk){
    map <int,int> ret;
    for(int i=0;i<first.size();i++){
        ret[ first[i] ]++;
    }
    for(int i=0;i<N;i++){
        if(msk & (1<<i)){
            ret[ open[i] ]--;
            for(int j=0;j<will[i].size();j++){
                ret[ will[i][j] ]++;
            }
        }
    }
    return ret;
}

vector <int> res;
int done [ (1<<20)+ 100];
int dfs(int msk){
    if(msk == lim){
        return 1;
    }
    int ret=0;
    map <int,int> have = find_it(msk);

    for(int i=0;i<N;i++){
        if(msk & (1<<i))continue; // already neya hoise
        if(have[ open[i] ]){
            if(done[ msk | (1<<i) ])continue;
            done[ msk | (1<<i) ]=1;
            int k = dfs(msk | (1<<i));
            if(k){
                res.pb(i+1);
                return 1;
            }
        }
    }
    return 0;
}

int main(){
    #if defined( faiyaz_pc )
        READ("D-small-attempt0.in");
        WRITE("ou.txt");
    #endif

    scanf("%d",&t);
    while(t--){
        printf("Case #%d: ",chk++);
        for(int i=0;i<505;i++){
            will[i].clear();
            init[i]=0;
            open[i]=0;
        }
        first.clear();
        ms(done,0);
        res.clear();
        cin>>K>>N;
        for(int i=0;i<K;i++){
            cin>>x;
            first.pb(x);
            init[x]=1;
        }
        for(int i=0;i<N;i++){
            cin>>op;
            open[i]=op;
            cin>>k;
            for(int j=0;j<k;j++){
                cin>>x;
                will[i].pb(x);
            }
        }
        lim= (1<<N)-1;
        dfs(0);
        reverse(all(res));
        for(int i=0;i<res.size();i++){
            if(i)cout<<" ";
            cout<<res[i];
        }
        if(res.size()==0){
            cout<<"IMPOSSIBLE";
        }
        cout<<endl;
    }
    return 0;
}
