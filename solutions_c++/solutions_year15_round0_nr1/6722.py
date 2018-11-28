/*
 *ID:   Cowboy
 *TASK: A. Standing Ovation
 *Judge: Codejam
 */
#include <bits/stdc++.h>
#define INF 0x7fffffff
#define PI 2*acos(0.0)
using namespace std;

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
    int T, n, res, acc, val, cas = 0;
    string str;
    for( cin>>T; cas<T; cas++){
        cin>>n;
        cin>>str;
        res = 0;
        acc = str[0]-'0';
        for( int i=1; i<str.size(); i++) {
            val = str[i]-'0';
            if( i>acc ){
                res+= i-acc;
                acc+= i-acc;
            }
            acc += val;
        }
        printf("Case #%d: %d\n", cas+1, res);
    }
    return 0;
}
