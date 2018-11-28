#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
#include <iostream>

const int maxn = ~0U>>1;
int t,d,p;
int ans;
std::priority_queue<int>q;

void dfs(std::priority_queue<int> &q, int tmp){
    if(tmp>=ans) return;
    int x = q.top();q.pop();
    ans = std::min(ans,tmp+x);
    for(int i=1;i*2<=x;i++){
        std::priority_queue<int> qq = q;
        qq.push(i),qq.push(x-i);
        dfs(qq,tmp+1);
    }
}
int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B2.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%d",&d);
        while(q.size()) q.pop();
        for(int i=1;i<=d;i++){
            scanf("%d",&p);
            q.push(p);
        }
        ans=maxn;
        dfs(q, 0);
        std::cerr<<ans<<std::endl;
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
