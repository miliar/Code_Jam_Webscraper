#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()


using namespace std;
vector<vector<char> > inp;
int r,c;
bool checkOk(int i, int j){
    if(inp[i][j] == '.'){
        return true;
    }
    pair<int,int> inc;
    char ch = inp[i][j];
    if(ch == '^'){
        inc = {-1,0};
    }
    if(ch == '>'){
        inc = {0,1};
    }
    if(ch == '<'){
        inc = {0, -1};
    }
    if(ch == 'v'){
        inc = {1, 0};
    }
    i += inc.ST;
    j += inc.ND;
    while(i >= 0 && i < r && j >= 0 && j < c){
        if(inp[i][j] != '.'){
            return true;
        }
        i += inc.ST;
        j += inc.ND;
    }
    return false;
}

bool canBetter(int i, int j){
    pair<int, int> dir[] = {
        {0, 1},
        {1,0},
        {-1,0},
        {0,-1}
    };
    int basei = i;
    int basej = j;
    REP(q,4){
        pair<int,int> inc = dir[q];
        i = basei;
        j = basej;
        i += inc.ST;
        j += inc.ND;
        while(i >= 0 && i < r && j >= 0 && j < c){
            if(inp[i][j] != '.'){
                return true;
            }
            i += inc.ST;
            j += inc.ND;
        }
    }
    return false;
}

int main()
{
    #define name "A-large"
    freopen(name ".in","r",stdin);
    freopen(name ".out","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    inp.resize(105, vector<char>(105));
    REP(q,t){
        cin>>r>>c;

        REP(i, r){
            string temp;
            cin>>temp;
            REP(j, (int)temp.size()){
                inp[i][j] = temp[j];
            }
        }
        int result = 0;
        REP(i, r){
            REP(j, c){
                if(checkOk(i,j)){
                    continue;
                }
                if(canBetter(i,j)){
                    result++;
                } else{
                    result = -1;
                    goto asd;
                }
            }
        }
        asd:
        cout<<"Case #"<<q + 1<<": ";
        if(result == -1){
            cout<<"IMPOSSIBLE";
        } else{
            cout<<result;
        }
        cout<<'\n';
    }
    return 0;
}

