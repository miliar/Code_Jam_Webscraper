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
vector <int> v;
int t,E,R,N;
int mem [20][20];
int dp(int idx,int have){
    if(idx==v.size()){
        return 0;
    }
    if(mem[idx][have] > -1){
        return mem[idx][have];
    }
    int ret=0;

    for(int i=0;i<=have;i++){
        ret= max(ret, i*v[idx]+ dp(idx+1,(have-i+R)%(E+1)));
    }
    return mem[idx][have]=ret;
}
int main(){
    #if defined( faiyaz_pc )
        READ("B-small-attempt0.in");
        WRITE("osmal.txt");
    #endif
    int x,chk=1;
    cin>>t;
    while(t--){
        cin>>E>>R>>N;
        v.clear();
        for(int i=0;i<N;i++){
            cin>>x;
            v.pb(x);
        }
        ms(mem,-1);
        printf("Case #%d: ",chk++);
        cout<<dp(0,E)<<endl;
    }
    return 0;
}
