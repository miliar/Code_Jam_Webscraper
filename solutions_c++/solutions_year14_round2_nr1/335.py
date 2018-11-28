    using namespace std;
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <string>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

#define SET(a,x) memset((a),(x),sizeof(a))
#define COPY(a,b) memcpy((a),(b),sizeof(a))
// set = 0
#define PB push_back
#define TR(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)

#define EXIST(c,x) (c.find(x)!=c.end())

typedef double LL;
typedef pair<int,int>II;
typedef pair<int,II>III;

#define ST first
#define ND second

typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<II>VII;
typedef vector<VII>VVII;

int ntest;
int n,res,cnt;
string s[128];
VI a[128];
VI b[128];

int ABS(int x){
    if(x > 0) return x;else return -x;

}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);

    cin >> ntest;

    FOR(test,1,ntest){
    
        cin >> n;
    
        FOR(i,1,n) cin >> s[i];

        FOR(i,1,n){
            a[i].clear();
            b[i].clear();

            int ls = s[i].length();

            int j = 0;
            
            cnt = 0;

            while(j < ls){
                j++;
                cnt++;

                a[i].PB(s[i][j-1] - 'a');
                b[i].PB(1);

                while( j < ls && s[i][j] == s[i][j-1]){
                    j++;
                    b[i][cnt-1] ++;
                }
            }
        }
        
        int haveres = 1;

        FOR(i,1,n) FOR(j,1,n) {
            if(a[i].size() != a[j].size()) {
                haveres = 0;
                break;
            }
            FOR(k,0,a[i].size()-1){
                if(a[i][k] != a[j][k]) {
                    haveres = 0;
                    break;
                }
            }
            if(haveres == 0) break;
        }
        if( !haveres )  cout <<"Case #"<<test<<": "<< "Fegla Won"<<endl;
        else{
            res = 0;
            FOR(i,1,a[1].size()){
                
                int mk = 11000;

                FOR(k,1,100){
                int t = 0;
                FOR(j,1,n) t += ABS(b[j][i-1] - k  );
                mk = min(mk,t);
                }
                res+= mk;
            }
            cout <<"Case #"<<test<<": "<< res<<endl;
        }
    }
    return 0;
}
