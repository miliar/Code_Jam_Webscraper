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
#define MAX 1005

int lim;

int dp(int num){
    if(num <= lim) return 0;

    int ret = inf;

    for(int i=1;i<num;i++){
        int half = i;
        int other = num - half;
        ret = min(ret, 1 + dp(half) + dp(other));
    }


    return ret;
}
vector <int> v;
int main(){
    #if defined( faiyaz_pc )
        READ("B-small-attempt2.in");
        WRITE("small.out");
    #endif

    int t, chk = 1, q, n;

    CIN;

    cin>>t;

    while(t--){
        cin>>n;

        v.clear();

        int a = 0, b = 0;
        int res = 0;
        for(int i=0;i<n;i++){
                cin>>q;
                res = max(res, q);
                v.pb(q);
        }


        for(int i=1;i<=1000;i++){
            int cst = i;
            lim = i;
            for(int j=0;j<v.size();j++){
                cst += dp(v[j]);
            }

            res = min(res, cst);
        }

        cout<<"Case #"<<chk++<<": "<<res<<"\n";
    }
    return 0;
}
