#include <algorithm>
#include <iostream>
#include <queue>
#include <cstdio>

using namespace std;
typedef pair<int, int> pair_q;


int main(){
#ifndef ONLINE_JUDGE
    	freopen("/Users/baidu/Desktop/A-large.in", "r", stdin);
    	freopen("/Users/baidu/Desktop/A-large.out", "w", stdout);
#endif
    int T, n, cas = 1;
    cin >> T;
    while (T--){
        cin >> n;
        priority_queue <pair_q> Q;
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            Q.push(make_pair(x, i));
        }
        printf("Case #%d:", cas++);
        while (!Q.empty()){
            if (Q.size() == 1){
                printf(" %c", Q.top().second + 'A');
                Q.pop();
            }else{
                pair_q a = Q.top();
                if (a.first == 1 && Q.size() == 3){
                    printf(" %c", a.second + 'A');
                    Q.pop();
                    continue;
                }
                Q.pop();
                if (a.first > 1){
                    Q.push(make_pair(a.first-1, a.second));
                }
                pair_q b = Q.top();
                Q.pop();
                if (b.first > 1){
                    Q.push(make_pair(b.first-1, b.second));
                }
                printf(" %c%c", a.second+'A', b.second+'A');
            }
        }
        printf("\n");
    }
    return 0;
}