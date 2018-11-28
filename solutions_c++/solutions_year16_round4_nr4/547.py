#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <cassert>
#include <set>
using namespace std;


const int N=10;

double pos[N];

string s[N];
string p[N];
string q[N];
vector<string> all[N];
int n;
int ret;

bool exist=false;

bool vis[N];
void check(int dep) {
    if (exist) return;
    if (dep>=n) return;
    bool can=false;
    for (int i=0;i<n;i++) {
        if (q[dep][i]=='1'&&!vis[i]) can=true;
    }
    if (!can) exist=true;
    for (int i=0;i<n;i++) {
        if (q[dep][i]!='1') continue;
        if (!vis[i]) {
            vis[i]=true;
            //cout<<"ddep "<<i<<endl;
            check(dep+1);
            vis[i]=false;
        }
    }
}

int calc() {
    int cnt=0;
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (s[i][j]!=p[i][j])
                cnt++;
        }
    }
    return cnt;
}
int cho[N];
void dfs(int dep) {
    if (dep>=n) {
        for (int i=0;i<n;i++)
            p[i]=all[i][cho[i]];
        bool quanju=true;
        //for (int i=0;i<n;i++) cout<<p[i]<<" ";cout<<endl;
        vector<int>num;
        for (int i=0;i<n;i++) num.push_back(i);
        do {
            for (int i=0;i<n;i++) q[i]=p[num[i]];
            exist=false;
            memset(vis,false,sizeof vis);
            check(0);
            if (exist) quanju=false;
            if (quanju==false) break;

        }while (next_permutation(num.begin(),num.end()));
        if (quanju) {
            ret=min(ret,calc());
        }
        return;
    }
    for (int i=0;i<all[dep].size();i++) {
        cho[dep]=i;
        dfs(dep+1);
    }
}
void get(int id,int dep,string ret) {
    if (dep>=n) {
        all[id].push_back(ret);
        return;
    }
    if (s[id][dep]=='1')
        get(id,dep+1,ret+'1');
    else {
        get(id,dep+1,ret+'0');
        get(id,dep+1,ret+'1');
    }
}
int main () {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
       scanf("%d",&n);
       for (int i=0;i<n;i++) {
        char t[10];
        scanf("%s",t);
        s[i]=string(t);
        all[i].clear();
       }
       for (int i=0;i<n;i++)
        get(i,0,"");
       ret=0x3f3f3f3f;
       dfs(0);
       printf("Case #%d: %d\n",cas,ret);
    }
    return 0;
}
