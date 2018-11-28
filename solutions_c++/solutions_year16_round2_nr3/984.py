#include "stdio.h"
#include "iostream"
#include "vector"
#include "set"
#include "algorithm"
#define state pair<string,string>
#define f first
#define s second
using namespace std;
int analyze(int n,vector<state> d);
void reset(int n);
void increment(int n);
vector<bool> check(16,false);
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("c-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++){
        int n,ans=0;
        scanf("%d",&n);
        reset(n);
        vector<state> d(n);
        for(int i=0;i<n;i++) cin>>d[i].f>>d[i].s;
        int limit=(1<<n);
        for(int i=0;i<limit;i++){
            ans=max(ans,analyze(n,d));
            increment(n);
        }
        printf("Case #%d: %d\n",l,ans);
    }
}
int analyze(int n,vector<state> d){
    int countx=0;
    set<string> p,q;
    for(int i=0;i<n;i++){
        if(check[i]){
            p.insert(d[i].f);
            q.insert(d[i].s);
        }
    }
    for(int i=0;i<n;i++){
        if(!check[i]){
            if(p.find(d[i].f)!=p.end()&&q.find(d[i].s)!=q.end()) countx++;
            else return -1;
        }
    }
    return countx;
}
void reset(int n){
    for(int i=0;i<n;i++) check[i]=false;
}
void increment(int n){
    for(int i=n-1;i>=0;i--){
        if(check[i]) check[i]=false;
        else{
            check[i]=true;
            return;
        }
    }
}
