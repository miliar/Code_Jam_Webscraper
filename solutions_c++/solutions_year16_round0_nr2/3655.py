#include<bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)
#define INF 1000000000
using namespace std;

int reverse(int n, int len){
    int ret = 0;
    REP(i, len)if((n&(1<<(len-i-1)))){
        ret|=(1)<<i;
    }
    return ret;
}

int step(int from, int by){
    int m = (1<<by)-1;
//    int tmp = from&m;
    int tmp = reverse(from, by);
    return (from&(~m))|(tmp^m);
}

int d[(1<<11)];


void testcase(int T){
    char s[12];
    scanf("%s", s);
    int blah = 0;

    for(int i = 0; s[i] != 0; i++){
        if(s[i]=='-')blah|=(1<<i);
    }
//    printf("%d\n", blah);
    printf("Case #%d: %d\n", T, d[blah]);
}

void bfs(){
    queue<int> q;
    d[0] = 0;
    q.push(0);
    while(!q.empty()){
        int tp = q.front();
        q.pop();
        int di = d[tp];
        REP(i, 11){
            int nw = step(tp, i);
//            printf("%d\n", nw);
            if(d[nw] > di+1){
                d[nw] = di+1;
                q.push(nw);
            }
        }
    }
}

int main(){
    REP(i, (1<<10))d[i] = INF;

    bfs();
//    printf("%d %d %d\n", reverse(15, 4), step(31, 5), step(31, 0));
    int t;
    scanf("%d", &t);
    REP(i, t)testcase(i+1);


    return 0;
}
