/*
Bismillahir Rahmanir Rahim
Coder: Ahmad Faiyaz
*/

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
#include <ctime>


# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-11
#define inf 1234567891
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

#define pb push_back
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define pii pair<int,int>
#define UNIQUE(c) (c).resize( unique( all(c) ) - (c).begin() )

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define CIN ios_base::sync_with_stdio(0);
///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;

map <int, int> pos;
vector <int> v;
int mx;
int n;
int lim;
int mem [(1<<12)][4][12];
int done [(1<<12)][4][12];
int c;
int dp(int msk, int f,int lst){
    /*
    for(int i=0;i<4;i++){
            cout<<!!(msk & (1<<i));
        }
        cout<<endl; */
    if(msk == lim) {
        return 0;
    }
    //cout<<mem[msk][f][lst]<<endl;
    if(done[msk][f][lst] == c) return mem[msk][f][lst];
    int idx = __builtin_popcount(msk);
    int ret = inf;
    for(int i=0;i<n;i++){
        if(msk & (1<<i)) continue;
        if(!f && lst!= -1 && v[i] < v[lst]) continue;
        if(f && lst != -1 && v[i] > v[lst]) continue;
        int cnt = 0;
        int nxtf = f;
        if(v[i] == mx) nxtf = 1;
        for(int j=0;j<n;j++){
            if(msk & (1<<j)){
                if(pos[v[j]] > pos[v[i]]) cnt++;
            }
        }
        int cur = pos[ v[i] ] + cnt;
        int add = abs(cur - idx);
        //cout<<add<<endl;
        ret = min(ret, add + dp( msk | (1<<i), nxtf, i));
    }
    mem[msk][f][lst] = ret;
    done[msk][f][lst] = c;
    return ret;
}


int main(){
    #if defined( faiyaz_pc )
        READ("B-small-attempt0.in");
        WRITE("small.txt");
    #endif
    int t, x, chk = 1;
    cin>>t;
    c = 0;
    while(t--){
        cin>>n;
        c++;
        pos.clear();
        v.clear();
        lim = (1<<n)-1;
        mx = 0;
        for(int i=0;i<n;i++){
            cin>>x;
            v.pb(x);
            pos[x]= i;
            mx = max(mx, x);
        }
        memset(mem, -1, sizeof(mem));
        cout<<"Case #"<<chk++<<": "<<dp(0, 0, -1)<<"\n";

    }
    return 0;
}
