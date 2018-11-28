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
   freopen("A-largeB.in", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    string num, res;
    int ord[] = {0, 2, 6, 8, 7, 5, 4, 9, 3,1};
    char rep[] = {'Z','O','W','T','F','V','X','S','G', 'I'};
    string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR"
                     , "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int n;
    cin>>n;
    for (int aux, cas = 0; cas < n; cas++) {
        cin>>num;
        vector<int>cnt(30, 0);
        for (char c : num) {
            cnt[c - 'A']++;
        }
        res = "";

        for (int i : ord) {
//            cout<< i <<" "<<cnt[rep[i]-'A']<<"\n";
            if (cnt[rep[i]-'A'] > 0) {
                aux = cnt[ rep[i] - 'A' ];
                for (char c : nums[i]) {
                    cnt[c - 'A'] -= aux;
                }
                for ( int j = 0; j < aux; j++) {
                    res.push_back(char(i+'0'));
                }
            }
        }
        sort(ALL(res));
        cout<<"Case #"<<cas+1<<": "<<res<<"\n";
    }
return 0;
}
