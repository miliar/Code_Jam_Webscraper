#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 1000;
bool vis[N];
int r;
void solve()
{
    CLR(vis,0);
    vector<int> ans;
    scanf("%d",&r);
    r--;
    for(int i = 0 ; i < 4 ; i ++){
        for(int j = 0 ; j < 4 ; j ++){
            int x;
            scanf("%d",&x);
            if(i == r){
                vis[x] = 1;
            }
        }
    }
    scanf("%d",&r);
    r--;
    for(int i = 0 ; i < 4 ; i ++){
        for(int j = 0 ; j < 4 ; j ++){
            int x;
            scanf("%d",&x);
            if(i == r){
                if(vis[x])ans.push_back(x);
            }
        }
    }
    if(ans.size() == 1){
        printf("%d\n",ans[0]);
    }else if(ans.size() == 0){
        printf("Volunteer cheated!\n");
    }else{
        printf("Bad magician!\n");
    }
}
int main()
{
   // freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);
    int cas = 0;
    int T;
    scanf("%d",&T);
    while(T--){
        cas ++ ;
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
