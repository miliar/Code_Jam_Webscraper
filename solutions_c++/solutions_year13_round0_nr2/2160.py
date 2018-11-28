#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define FOR(a,b,c) for(int (a)=(b);(a)<(c);(a)++)
#define sor(a) sort((a).begin(),(a).end())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    FOR(tc,1,t+1){
        cout << "Case #" << tc << ": ";
        int n,m;
        cin >> n >> m;
        int grid[n][m];
        FOR(i,0,n)
            FOR(j,0,m)
                cin >> grid[i][j];
        bool valid = true;
        FOR(i,0,n){
            FOR(j,0,m){
                bool validH=true;
                bool validV= true;
                for(int k=0;k<n && validV;k++)
                    validV &= (grid[k][j]<= grid[i][j]);

                if(!validV)
                    for(int k=0;k<m && validH;k++)
                        validH &= (grid[i][k]<= grid[i][j]);
                valid &= (validH || validV);
                if(!valid)
                    break;
            }
            if(!valid)
                break;
        }

        if(valid)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
