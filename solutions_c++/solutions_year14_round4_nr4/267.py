#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;

int ans = 0 ;
int ansc=0;
vector<string> v;
int assi[10];
int ctr[10];
set<string> all[10];
void dfs(int now,int cnt,int n){
    if(now==cnt){
        for(int i = 0 ; i < n ; ++ i )if(ctr[i]==0)return;
        for(int i = 0 ; i < n ; ++ i ) all[i].clear();
        for(int i = 0 ; i < cnt ; ++ i ){
            string s="";
            for(int j = 0 ; j < v[i].size() ; ++ j ){
                s.push_back(v[i][j]);
                all[assi[i]].insert(s);
            }
        }

        int r=n;
        for(int i = 0 ; i < n ; ++ i ) r+=all[i].size();
        if(r==ans)ansc++;
        else if(r>ans) {
            ansc=1;
            ans=r;
        }
        return;
    }
    for(int i=0;i<n;++i){
        assi[now]=i;
        ctr[i]++;
        dfs(now+1,cnt,n);
        ctr[i]--;
    }
}
void solve(){
    ans=0;
    int m,n;
    scanf("%d %d",&m,&n);
    v.clear();
    for(int i =0 ; i  < m ; ++ i ){
        string str;
        cin >> str;
        v.push_back(str);
    }
    dfs(0,m,n);
    printf("%d %d\n",ans,ansc);
}

int main(){
    freopen("D-small-attempt0"".in","r",stdin);
    freopen("D-small-attempt0"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
