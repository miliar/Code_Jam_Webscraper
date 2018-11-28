#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>
using namespace std;

int vis[10];
int ans[1000000+5];

int work(int n){
    int cnt=0;
    memset(vis,0,sizeof(vis));
    for(int i=1;i<=n;i++){
        int tmp=n*i;
        while(tmp){
            int x=tmp%10;
            if(vis[x]==0){
                vis[x]=1;
                cnt++;
                if(cnt==10)return n*i;
            }
            tmp/=10;

        }
    }
    return -1;
}

int main(){
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    memset(ans,0,sizeof(ans));
    ans[1]=10,ans[2]=90,ans[3]=30,ans[4]=92,ans[5]=90,ans[6]=90,ans[7]=70,ans[8]=96,ans[9]=90;
    ans[12]=156,ans[14]=238,ans[20]=900,ans[25]=900;

    int T,n;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&n);
        if(n==0){printf("Case #%d: INSOMNIA\n",t);continue;}

        if(ans[n]==0)ans[n]=work(n);
        printf("Case #%d: %d\n",t,ans[n]);
    }
    return 0;
}
