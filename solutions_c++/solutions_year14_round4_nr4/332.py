#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

const int MOD = 1000000007;
char s[20][20];
int N,M,c[5],a[5][10],way,ans,l[20];

typedef struct A{
    char ch;
    int nxt;
}AA;
AA tri[1005];

int rec(vector <int> v,int lv){
    if(v.size()==0)
        return 0;
    if(v.size()==1){
        int len = l[v[0]];
        return len-lv;
    }
    //printf("lv = %d\n",lv);
    int ret = 0;
    vector <int> vv[30];
    for(int i=0;i<v.size();i++){
        int x = v[i];
        //printf("x = %d, %d\n",x,l[x]);
        if(lv<l[x])
            vv[s[x][lv]-'A'].push_back(v[i]);
    }
    for(int i=0;i<30;i++){
        if(vv[i].size()!=0){
            ret++;
            ret += rec(vv[i],lv+1);
        }
    }
    return ret;
}
int test(){
    int ret = 0;
    for(int i=0;i<M;i++){
        vector <int> v;
        for(int j=0;j<c[i];j++)
            v.push_back(a[i][j]);
        ret += rec(v,0)+1;
    }
    return ret;
}
void dfs(int lv){
    //printf("lv = %d\n",lv);
    if(lv==N){
        for(int i=0;i<M;i++)
            if(c[i]==0)
                return;
        int tmp = test();
        if(tmp>ans){
            ans = tmp;
            way = 1;
        }else if(tmp==ans){
            way++;
        }
        return ;
    }
    for(int b=0;b<M;b++){
        a[b][c[b]] = lv;
        c[b]++;
        dfs(lv+1);
        c[b]--;
    }
}

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    scanf(" %d",&T);
    for(int t=0;t<T && scanf(" %d %d",&N,&M)==2;t++){
        for(int i=0;i<N;i++){
            scanf(" %s",s[i]);
            l[i] = strlen(s[i]);
        }
        memset(c,0,sizeof(c));
        ans = 0;
        way = 0;
        /*vector <int> v;
        for(int i=0;i<N;i++)
            v.push_back(i);
        printf("%d\n",rec(v,0));*/
        dfs(0);
        printf("Case #%d: %d %d\n",t+1,ans,way);
    }

    return 0;
}
