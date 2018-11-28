#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
int ans;
bool cmp(int a, int b){
    return a>b;
}
void DFS(vector<int> &now, int tm){
    if(tm >= ans) return;
    if(now.size() == 0){
        ans = min(ans, tm);
        return;
    }
    int Size = now.size();
    vector<int> nxt;

    for(int i=0;i<Size;i++){
        if(now[i] > 1) nxt.push_back(now[i]-1);
    }
    DFS(nxt, tm+1);
    if( now[0] > 1 ){
        for(int k=1;k<=now[0]/2;k++){
            nxt.clear();        
            nxt.push_back(k);
            nxt.push_back(now[0]-k);
            for(int i=1;i<Size;i++) nxt.push_back(now[i]);
            sort(nxt.begin(), nxt.end(), cmp);
            DFS(nxt, tm+1);
        }
    }
}
int main(){
    int T, n;
    vector<int> num;
    scanf("%d", &T);
    int f = 0, x;
    while(T--){
        num.clear();
        ans = 0;
        scanf("%d", &n);
        for(int i=0;i<n;i++){
            scanf("%d", &x);
            num.push_back(x);
            ans = max(ans, x);
        }
        sort(num.begin(), num.end(), cmp);
        DFS(num, 0);
        printf("Case #%d: %d\n", ++f, ans);
    }

    return 0;
}
