#include <iostream>
#include <cstdio>
using namespace std;

int _;
int N,M;
string c[10];
int cnt;
int Max,ans;
int d[10];

int lx(char c){
    return c-'A';
}

struct node{
    node* c[26];
    node(){
        for (int i=0;i<26;i++) c[i] = NULL;
    }
};

node *root[100];

void ins(string &s,int p){
    node *now = root[p];
    if (!now){
        now = root[p] = new node();
        cnt++;
    }
    for (string::iterator k=s.begin();k!=s.end();k++){
        int pp = lx(*k);
        if(!now->c[pp]){
            now -> c[pp] = new node();
            cnt++;
        }
        now = now -> c[pp];
    }
}

void dof(node *now){
    if (now==NULL) return;
    for (int i=0;i<26;i++) dof(now->c[i]);
    delete now;
}

void work(){
    for (int i=1;i<=N;i++){
        dof(root[i]);
    }
    cnt=0;
    for (int i=1;i<=N;i++){
        root[i] = NULL;
    }
    for (int i=1;i<=M;i++){
        ins(c[i],d[i]);
    }
    if (cnt > Max){
        Max = cnt;
        ans = 1;
    } else if (cnt==Max) ans++;
}

void dfs(int i){
    if (i>M){
        work();
        return;
    }
    for(int ii=1;ii<=N;ii++){
        d[i]=ii;
        dfs(i+1);
    }
}

int main(){
    //freopen("in.txt","r",stdin);
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    scanf("%d",&_);
    int cas = 0;
    while(_--){
        Max = -1;
        scanf("%d%d",&M,&N);
        for (int i=1;i<=M;i++) cin >> c[i];
        dfs(1);
        printf("Case #%d: %d %d\n",++cas,Max,ans);
    }
}
