#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

string a[10005];
int b[1000];

int n,m,ans,now,num;
struct Node{
    char ch;
    vector<Node*> son;
    Node(){ ch = '!'; }
    Node(char x){ ch = x; }
};
void insert(Node* root, string p){
    for (int i = 0; i < p.size(); i++){
        bool ok = false;
        for (int j = 0; j < root -> son.size(); j++)
            if (p[i] == root -> son[j] -> ch){
                root = root->son[j];
                ok = true;
                break;
            }
        if (!ok){
            now++;
            root->son.push_back(new Node(p[i]));
            root = root->son[root->son.size() - 1];
        }
    }
}
int cnt[10];
void check(){
    memset(cnt, 0,sizeof cnt);
    for (int i = 1; i <= n; i++)
        cnt[b[i]] ++;
    for (int i = 1; i <= m; i++)
        if (cnt[i] == 0) return;
    now = 0;
    for (int i = 1; i <= m; i++){
        Node *root = new Node;
        now++;
        for (int j = 1; j <= n; j++)
            if (b[j] == i)
                insert(root, a[j]);
    }
    if (now > ans){ans = now;num=1;}
    else if (now==ans)num++;
}
void dfs(int t){
    if (t > n) check(); else {
        for (int i = 1; i <= m; i++){
            b[t] = i;
            dfs(t + 1);
        }
    }
}
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dsmall.out","w",stdout);
    int T; cin >> T;

    for (int o = 1; o <= T; o++){
        cin >> n >> m;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        ans = 0, num = 0;
        dfs(1);
        printf("Case #%d: %d %d\n", o, ans,num);
    }

}
