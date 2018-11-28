#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <limits.h>
#include <stdlib.h>
#include <algorithm>
#include <set>
using namespace std;

const int MAXLN = 1e5 + 5;
const int MAXN = MAXLN << 1;
int N , L,ans = 0 ,tp;
set<int > cover_set;

struct STree
{
    int cover;
    int l,r;
}t[MAXN<<2];

struct L{
    int li,num;
    bool operator < (const L &r) const{
        return li < r.li;
    };
}line[MAXLN<<1];
int post[MAXLN][2];
int cnt = 0;

void pushdown(int p){
    if(t[p].cover){
        int ls = p << 1;
        int rs = ls + 1;
        t[ls].cover = t[p].cover;
        t[rs].cover = t[p].cover;
        t[p].cover = 0;
        // cout<<t[p].cover<<" "<<p<<" "<<t[p].l<<" "<<t[p].r<<endl;
        // cout<<t[ls].cover<<" "<<ls<<endl;
        // cout<<t[rs].cover<<" "<<rs<<endl;
    }
}

void build(int p , int l ,int r){
    t[p].cover = 0;
    t[p].l = l;
    t[p].r = r;
    if(l+1>=r)
        return;
    int mid = (l + r)>>1;
    build(p<<1,l,mid);
    build(p<<1|1,mid,r);
}

void modify(int p, int l,int r,int c){
    if(t[p].l == l && t[p].r == r){
        //cout<<l<<" "<<r<<" "<<c<<endl; 
        //cout<<t[8].cover<<" "<<p<<endl;
        t[p].cover = c;
        return;
    }
    pushdown(p);
    int mid = (t[p].l + t[p].r)>>1;
    if(l>=mid)
        modify(p<<1|1,l,r,c);
    else if(r <= mid)
        modify(p<<1,l,r,c);
    else
    {
        modify(p<<1,l,mid,c);
        modify(p<<1|1,mid,r,c);
    }   
}

void read(){
    cin>>N>>L;
    for(int i = 1 ; i<=N ; i++)
    {
        scanf("%d %d",&post[i][0],&post[i][1]);
        line[i<<1].li = post[i][0];
        line[i<<1].num = i;
        line[i<<1|1].li = post[i][1];
        line[i<<1|1].num = -i;
    }
    sort(line + 2,line + 2 + 2 * N);
    tp = 1;
    int temp = line[2].li;
    for(int i = 2; i<= 2 * N + 1 ;i++){
        if(line[i].li != temp){
            tp++;
            temp = line[i].li;
        }
        if(line[i].num > 0)
            post[line[i].num][0] = tp; 
        
        else
            post[-line[i].num][1] = tp;        
    }
}

void dfs(int p){
    if(t[p].cover)
    {
        set<int>::iterator it;
        it = cover_set.find(t[p].cover);
        if(it == cover_set.end())
        {
            cover_set.insert(t[p].cover);
            ans++;
        }
        return;
    }
    if(t[p].l + 1 >= t[p].r)
        return;
    dfs(p<<1);
    dfs(p<<1|1);
}

void solve(){
    for(int i = 1 ; i<= N ; i++){
        //cout<<post[i][0]<<" "<<post[i][1]<<" "<<i<<endl;
        modify(1,post[i][0],post[i][1],i);
    }
    dfs(1);
    cout<<ans<<endl;
}

int main(){
    read();
    build(1,1,tp);
    solve();
    set<int>::iterator it;
    // for(it = cover_set.begin();it!=cover_set.end();it++)
        // cout<<*it<<endl;
    return 0;
}