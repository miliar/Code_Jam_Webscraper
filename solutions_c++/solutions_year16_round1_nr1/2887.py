/*
 *ID:   Cowboy
 *TASK:
 *Judge:
 */
#include <bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef pair<int, int> II;
typedef vector<int> VI;
typedef vector<II> VII;

int main( ){
#ifndef ONLINE_JUDGE
   freopen("A-large.in", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    int T, cas = 0;
    for(cin>>T; cas < T; cas++){
        string res, query;
        cin>>query;
        res = query[0];
        for (int i = 1; i < query.size(); i++) {
            if(query[i] >= res[0]){
                res = query[i] + res;
            } else {
                res += query[i];
            }
        }
        cout<<"Case #"<<cas+1<<": "<<res<<"\n";
    }
return 0;
}
