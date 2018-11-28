#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int calc(){
    int n, s;
    vector<int> V;
    priority_queue<int> Q;
    scanf("%d %d", &n, &s);
    for(int i = 0; i < n; ++i){
        int val;
        scanf("%d", &val);
        V.push_back(val);
    }
    sort(V.begin(), V.end());
    int cnt = 0;
    for(int i = n - 1; i >= 0; --i){
        if(Q.empty()){
            if(V[i] == s){
                cnt++;
                continue;
            }else{
                Q.push(s - V[i]);
                cnt++;
            }
        }else{
            if(Q.top() >= V[i]){
                Q.pop();
            }else{
                Q.push(s - V[i]);
                cnt++;
            }
        }
    }
    return cnt;
}

int main(){
    int allt;
    scanf("%d", &allt);
    for(int i = 1; i <= allt; ++i){
        printf("Case #%d: %d\n", i, calc());
    }
    return 0;
}