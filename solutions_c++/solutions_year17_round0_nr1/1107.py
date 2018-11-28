/*************************************************************************
	> File Name: A.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月08日 星期六 11时20分51秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn=1000+10;
char s[maxn];
int k,vis[maxn];

void solve(int idx){
    for(int i=idx;i<idx+k;i++)
        vis[i]^=1;
}

int main(){
    //ios::sync_with_stdio(false);
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int T;scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        memset(vis,0,sizeof(vis));
        scanf("%s%d",s,&k);
        int len=strlen(s),ans=0;
        for(int i=0;i<=len-k;i++){
            if(vis[i] && s[i]=='+' || !vis[i] && s[i]=='-')
                solve(i),ans++;
        }
        bool f=true;
        for(int i=len-k+1;i<len;i++)
            if(vis[i] && s[i]=='+' || !vis[i] && s[i]=='-'){
                f=false;
                break;
            }
        if(!f)printf("Case #%d: IMPOSSIBLE\n",kase);
        else printf("Case #%d: %d\n",kase,ans);
    }
    return 0;
}
