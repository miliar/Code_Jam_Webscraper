#include <iostream>
#include <algorithm>
#include <cstring>
#include <memory.h>
#include <map>
#include <stdio.h>
const int maxn=100100;

using namespace std;

struct Node
{
    Node *son[26];
    int val;
}node[maxn ],*root;

int tot;
void Init(int k)
{
    memset(node[k].son, 0, sizeof(node[k].son) );
    node[k].val=0;
}
//初始 tot=0,Init(tot), root=&node[tot++];
void InitRoot(){
    tot = 0;
    Init(tot);
    root = &node[tot++];
}
void Insert(const char *s, int val)
{
    Node *r=root;
    int len=strlen(s);
    for(int i=0; i<len; i++ ){
        int id=s[i]-'A'; //要视情况定
        if( r->son[id]==0  ){
            Init(tot);
            r->son[id]=&node[tot++];
        }
        r=r->son[id];
        if( i==len-1 )
            r->val=val;//标记串尾
    }
}


string str[11];
int belong[11];
int n, m;
int mx = 0;
map<int, int> Map;

void getNodes(){
//    for(int i = 0; i < m; ++i) cout<<belong[i];
//    cout<<endl;
    int sum = 0;
    for(int k = 0; k < n; ++k){
//        cout<<"k="<<k<<endl;
        InitRoot();
        bool flag = false;
        for(int i = 0; i < m; ++i){
            if( belong[i] == k ){
//                cout<<"insert"<<i<<endl;
                Insert(str[i].c_str(), 1 );
                flag = true;
            }
        }
        if( flag )
            sum += tot;
    }
//    cout<<sum<<"==="<<endl;
//    system("pause");
    mx = max(mx, sum);
    Map[sum]++;

}

void dfs(int dep){
    if( dep == m ){
        getNodes();
        return;
    }
    for(int p = 0; p < n; ++p){
        belong[dep] = p;
        dfs(dep + 1);
    }
}

void solve(){
    Map.clear();    mx = 0;
    dfs(0);
}
int main()
{
    freopen("D0.in", "r", stdin );
    freopen("D0.out", "w", stdout );
    int t;
    cin>>t;
    int tno = 0;
    while( t-- ){
        cin>>m>>n;
        for(int i = 0; i < m; ++i)
            cin>>str[i];
        solve();
        printf("Case #%d: %d %d\n", ++tno, mx, Map[mx] );
    }
    return 0;
}
