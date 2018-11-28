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

int row [104], col [105];

int grid [105][105];


int main(){
    #if defined( faiyaz_pc )
        READ("B-large.in");
        WRITE("B_large.txt");
    #endif
    int t,chk=1,n,m;
    cin>>t;
    while(t--){
        cin>>n>>m;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>grid[i][j];
            }
        }

        for(int i=0;i<103;i++){
            row[i]=col[i]=0;
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                row[i]= max(row[i],grid[i][j]);
            }
        }

        for(int j=0;j<m;j++){
            for(int i=0;i<n;i++){
                col[j]= max(col[j],grid[i][j]);
            }
        };
        int ok=1;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==row[i] || grid[i][j]==col[j]){
                    continue;
                }
                ok=0;
            }
        }
        printf("Case #%d: ",chk++);
        if(ok){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}
