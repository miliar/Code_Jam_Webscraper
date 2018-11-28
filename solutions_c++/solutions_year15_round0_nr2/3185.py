#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

const int MAXD = 1000 + 10;
int d;
int p[MAXD];

int main() {    
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &d);
        int ans = 0;        
        for (int i = 0; i < d; i++) {
            scanf("%d", p + i);
            if (p[i] > ans) ans = p[i];
            //p[i] = -p[i];
        }
        //sort(p, p + d);
        //for (int i = 0; i < d; i++) p[i] = -p[i];        
        int maxv = ans;
        /*
        for (int i = 1; i <= maxv; i++) {
            priority_queue<int> q;
            for (int j = 0; j < d; j++) q.push(p[j]);            
            for (int j = 0; j < i; j++) {
                int cv = q.top();
                q.pop();
                q.push(cv / 2);
                q.push(cv - cv / 2);
            }
            ans = min(ans, q.top() + i);
        }
        */
        for (int i = 1; i <= maxv; i++) {
            int tcnt = 0;
            for (int j = 0; j < d; j++)
                if (p[j] > i) {
                    tcnt += (p[j] - 1) / i;
                }
            ans = min(ans, tcnt + i);
        }
        printf("Case #%d: %d\n", t, ans);                
    }
}

