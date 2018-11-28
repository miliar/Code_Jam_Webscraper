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
vector <double> v1, v2;
int lim;
int mem1 [(1<<20)+5];
int dp1(int msk){
    if(msk == lim) return 0;
    if(mem1[msk] > -1) return mem1[msk];
    int ret = 0;

    for(int i=0;i<v1.size();i++){
        if(msk & (1<<i)) continue;
        int ok = 0;
        for(int j=0;j<v2.size();j++){
            if(msk & (1<<(v1.size()+j))) continue;
            if(v2[j] > v1[i]){
                ok =1 ;
                ret = max(ret, dp1(msk | (1<<i) | (1<<(v1.size()+j))));
            }
        }
        if(!ok){
            for(int j=0;j<v2.size();j++){
                if(msk & (1<<(v1.size()+j))) continue;
                ret = max(ret,1 + dp1(msk|(1<<i)| (1<<(v1.size()+j))));
            }
        }
    }

    return mem1[msk]=ret;
}


int mem [(1<<20)+5];
int dp2(int msk){
    if(msk == lim) return 0;
    if(mem[msk] > -1) return mem[msk];
    int ret = 0;

    for(int i=0;i<v1.size();i++){
        if(msk & (1<<i)) continue;
        int ok = 0;
        for(int j=0;j<v2.size();j++){
            if(msk & (1<<(v1.size()+j))) continue;
            if(v2[j] > v1[i]){
                ok =1 ;
                ret = max(ret, dp2(msk| (1<<i)| (1<<(v1.size()+j))));
                break;
            }
        }
        if(!ok){
            for(int j=0;j<v2.size();j++){
                if(msk & (1<<(v1.size()+j))) continue;
                ok =1 ;
                ret = max(ret, 1 + dp2(msk|(1<<i)| (1<<(v1.size()+j))));
                break;
            }
        }
    }

    return mem[msk]=ret;
}

int main(){
    #if defined( faiyaz_pc )
        READ("D-small-attempt0.in");
        WRITE("D-small.out");
    #endif
    int t;
    CIN;
    double x;
    cin>>t;
    int n;
    int chk= 1;
    while(t--){
        ms(mem, -1);
        ms(mem1, -1);
        cin>>n;
        v1.clear();
        v2.clear();
        for(int i=0;i<n;i++){
            cin>>x;
            v1.pb(x);
        }
        for(int i=0;i<n;i++){
            cin>>x;
            v2.pb(x);
        }

        sort(all(v1));
        sort(all(v2));

        lim = (1<<(2*n))-1;
        cout<<"Case #"<<chk++<<": ";
        cout<<dp1(0)<<" ";
        cout<<dp2(0)<<"\n";

    }
    return 0;
}
