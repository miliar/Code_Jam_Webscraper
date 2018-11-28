#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <fstream>
using namespace std;
vector<vector<int> > adj;
bool visited[100000];//dfs쓸거면  visited 초기화;
int parent[100001];
int rnk[100001];
struct FenWick{
    vector<int> tree;
    FenWick(int n): tree(n+1){}
    int sum(int pos){
        ++pos;
        int ret=0;
        while(pos>0){
            ret+=tree[pos];
            pos&=(pos-1);
        }
        return ret;
    }
    void add(int pos,int val){
        ++pos;
        while(pos<tree.size()){
            tree[pos]+=val;
            pos+=(pos&-pos);
        }
    }
};
int find(int u){
    if(u==parent[u])
        return u;
    return parent[u]=find(parent[u]);
}
void merge(int u,int v){
    u=find(u);v=find(v);
    if(u==v)
        return ;
    if(rnk[u]>rnk[v])
        swap(u,v);
    parent[u]=v;
    if(rnk[u]==rnk[v])++rnk[v];
}
void initUnionFind(int n){
    for(int i=0;i<=n;i++)
    {    parent[i]=i;
        rnk[i]=1;
    }
}
unsigned GCD(unsigned u, unsigned v) {
    while ( v != 0) {
        unsigned r = u % v;
        u = v;
        v = r;
    }
    return u;
}
void dfs(int here){
    visited[here]=true;
    int there;
    for(int i=0;i<adj[here].size();i++){
        there=adj[here][i];
        if(!visited[there]){
            dfs(there);
        }
    }
}


int main(){
    ofstream fout("out.out");
    ifstream fcin("B-large.in");

    int testCase;fcin>>testCase;
    int n;
    for(int t=1;t<=testCase;t++){
        map<int,int> m;
        map<int,int>::iterator it;
        vector<int> ans;
        
        fcin>>n;
        int num;
        int loop=2*n-1;
        for(int i=0;i<loop;i++){
            for(int j=0;j<n;j++){
                fcin>>num;
                m[num]++;
            }
        }
        for(it=m.begin();it!=m.end();it++){
            if((it->second)%2==1)
                ans.push_back(it->first);
        }
        fout<<"Case #"<<t<<": ";
        for(int i=0;i<ans.size();i++){
            fout<<ans[i]<<' ';
        }
        fout<<endl;
    }

    return 0;
}
