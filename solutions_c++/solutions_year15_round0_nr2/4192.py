#include <iostream>
#include <cstdio>
#include <climits>
using namespace std;

int a[1100],N,ans;


int main(){
    freopen("/Users/jiangzefan/code/B/B/input.txt","r",stdin);
    freopen("/Users/jiangzefan/code/B/B/output.txt","w",stdout);
    int _,__;
    scanf("%d",&_);
    for (__=1;__<=_;__++){
        scanf("%d",&N);
        for (int i=0;i<N;i++){
            scanf("%d",&a[i]);
        }
        ans=INT_MAX;
        for (int i=1;i<=1000;i++){
            int t=0;
            for (int j=0;j<N;j++){
                t+=(a[j]-1)/i;
            }
            ans=min(ans,i+t);
        }
        printf("Case #%d: %d\n",__,ans);
    }
    
}