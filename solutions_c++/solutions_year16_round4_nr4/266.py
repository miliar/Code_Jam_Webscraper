#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#define maxn 500010
using namespace std;
struct edge{
    int to,next;
}e[maxn<<1];
int box[maxn],cnt;
void init(){
    memset(box,-1,sizeof(box));
    cnt=0;
}
void add(int from,int to){
    e[cnt].to=to;
    e[cnt].next=box[from];
    box[from]=cnt++;
}
vector<int> vec;
void dfs(int now,int fa,int dep){
    int tru=0;
    for(int t=box[now];t+1;t=e[t].next){
        int v=e[t].to;
        if(v!=fa){
            tru=1;
            dfs(v,now,dep+1);
        }
    }
    if(!tru)//leaf
        vec.push_back(dep);
}
int main()
{
    freopen("dd.txt","r",stdin);
    init();
    int n;
    scanf("%d",&n);
    for(int i=1;i<n;i++){
        int x,y;
        scanf("%d%d",&x,&y);
        add(x,y);
        add(y,x);
    }
    int ans=0;
    for(int t=box[1];t+1;t=e[t].next){
        int v=e[t].to;
        vec.clear();
        dfs(v,1,0);
        sort(vec.begin(),vec.end());
        int size=vec.size(),pre=-1;
        for(int i=0;i<size;i++){
            if(pre>=vec[i]){
                pre++;
            }
            else
                pre=vec[i];
        }
        ans=max(ans,pre+1);
    }
    cout<<ans<<endl;
    return 0;
}
