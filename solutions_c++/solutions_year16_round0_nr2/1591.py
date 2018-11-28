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

long long solve(string str) {
    str += '+';
    long long res = 0;
    for (int i = 1; i < str.size(); i++) {
        if (str[i - 1] != str[i]) {
            res++;
        }
    }
    return res;
}

int main( ){
#ifndef ONLINE_JUDGE
   freopen("B-large.in", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    int T;
    cin>>T;
    string str;
    for (int cas = 0; cas < T; cas++) {
        cin>>str;
        cout<<"Case #"<<cas+1<<": "<<solve(str)<<"\n";
    }
return 0;
}
