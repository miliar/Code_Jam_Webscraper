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
    int T;
    long long num, aux, last;
    cin>>T;
    for (int cas = 0; cas < T; cas++) {
        cin>>num;
        bitset<10>cnt;
        last = -1;
        for (int i = 1; i <= 1000; i++) {
            aux = i*num;
            //cout<<aux<<"\n";
            while (aux) {
                cnt[aux%10] = 1;
                aux/=10;
            }
            if (cnt.count() == 10) {
                last = i*num;
                break;
            }
        }

        cout<<"Case #"<<cas + 1<<": ";
        if (last != -1) {
            cout<<last<<"\n";
        } else {
            cout<<"INSOMNIA\n";
        }
    }
return 0;
}
