#include <map>
#include <climits>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define DBG(e) cout<<(#e)<<" : "<<e<<endl
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define CLEAR(v,i) memset(v,i,sizeof v)
#define ALL(x) x.begin(),x.end()
#define pb  push_back
#define pr pair<int,int>
#define SZ(x) int((x).size())


typedef long long LL;

int main()
{
    int tests;
    cin>>tests;
    FOR(tt,1,tests+1)
    {
        int n,m;
        cin>>n>>m;
        int mat[101][101];
        int mx=0;
        FOR(i,0,n) FOR(j,0,m) {cin>>mat[i][j];mx=max(mx,mat[i][j]);}
        int cur[101][101];
        FOR(i,0,n) FOR(j,0,m) cur[i][j]=mx;
        for(int val=mx-1;val>=1;val--){
            FOR(i,0,n){
                bool yes=1;
                FOR(j,0,m) if(mat[i][j]!=val) yes=0;
                if(yes) FOR(j,0,m) cur[i][j]=val;
            }
            FOR(i,0,m){
                bool yes=1;
                FOR(j,0,n) if(mat[j][i]!=val) yes=0;
                if(yes) FOR(j,0,n) cur[j][i]=val;
            }
        }
        bool found=1;
        FOR(i,0,n) FOR(j,0,m) if(mat[i][j]!=cur[i][j]) found=0;
        cout<<"Case #"<<tt<<": ";
        if(found) cout<<"YES\n";
        else cout<<"NO\n";
    }
}
