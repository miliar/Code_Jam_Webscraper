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
#define MAX 10004
char grid [MAX][MAX];
bool gridNeg [MAX][MAX];
char tr [255][255];
bool neg [255][255];

int main(){
    #if defined( faiyaz_pc )
        READ("C-small-attempt0.in");
        WRITE("small.out");
    #endif

    tr['1']['1'] = '1';
    tr['1']['i'] = 'i';
    tr['1']['j'] = 'j';
    tr['1']['k'] = 'k';

    tr['i']['1'] = 'i';
    tr['i']['i'] = '1'; neg['i']['i'] = 1;
    tr['i']['j'] = 'k';
    tr['i']['k'] = 'j'; neg['i']['k'] = 1;

    tr['j']['1'] = 'j';
    tr['j']['i'] = 'k'; neg['j']['i'] = 1;
    tr['j']['j'] = '1'; neg['j']['j'] = 1;
    tr['j']['k'] = 'i';

    tr['k']['1'] = 'k';
    tr['k']['i'] = 'j';
    tr['k']['j'] = 'i';neg['k']['j'] = 1;
    tr['k']['k'] = '1';neg['k']['k'] = 1;

    int t, l, x, chk = 1;

    string s, ss;

    CIN;

    cin>>t;

    while(t--){
        cin>>l>>x;

        cin>>s;

        ms(gridNeg, 0);

        ss = "";

        for(int i = 0; i < x;i++) ss += s;

        for(int i=0;i<ss.size();i++){
            char xx = '1';
            bool ng = 0;
            for(int j=i;j<ss.size();j++){
                    char a = ss[j];
                    ng ^= neg[xx][a];
                    xx  = tr[xx][a];

                    gridNeg[i][j] = ng;
                    grid[i][j] = xx;
            }
        }

 //       cout<<"here"<<endl;

        bool ok = 0;
        for(int i=0;i<ss.size() && !ok;i++){
            for(int j=i+1;j<ss.size()-1 && !ok;j++){
                int l = i;
                int r = j;

                // 1 -> l, l+1->r, r+1 -> ss.size()-1

                char a = grid[0][l];
                bool aa = gridNeg[0][l];
                char b = grid[l+1][j];
                bool bb = gridNeg[l+1][j];
                char c = grid[j+1][ss.size()-1];
                bool cc = gridNeg[j+1][ss.size()-1];

               // cout<<l<<" "<<r<<" "<<a<<" "<<b<<" "<<c<<" "<<aa<<" "<<bb<<" "<<cc<<endl;
                if(a == 'i' && !aa && b == 'j' && !bb && c == 'k' && !cc){
                    ok = 1;
                    break;
                }
            }
        }

        cout<<"Case #"<<chk++<<": ";
        if(ok) cout<<"YES\n";
        else cout<<"NO\n";
    }




    return 0;
}
