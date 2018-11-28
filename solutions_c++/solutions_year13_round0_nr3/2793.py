#include    <iostream>
#include    <cstdio>
#include    <cstdlib>
#include    <cstring>
#include    <cmath>
#include    <algorithm>
#include    <vector>
#include    <list>
#include    <queue>
#include    <stack>
#include    <map>
#include    <set>
#include    <utility>
#include    <climits>
#include    <cfloat>
#include    <cassert>
#define     read(n)         scanf("%d",&n)
#define     read2(n,m)      scanf("%d%d",&n,&m)
#define     read3(n,m,l)    scanf("%d%d%d",&n,&m,&l)
#define     readull(n)      scanf("%llu",&n)
#define     readll(n)       scanf("%lld",&n)
#define     init(mem)       memset(mem,0,sizeof(mem))
#define     ull             unsigned long long int
#define     ll              long long int
#define     vi              vector<int>
#define     vs              vector<string>
using namespace std;
//std::cout.sync_with_stdio(false);

bool fair(ll N){
    char num[20];
    sprintf(num,"%lld\0",N);
    int n=strlen(num);
    for(int i=0;i<n/2;i++){
        if(num[i]!=num[n-1-i]) return false;
    }
    return true;
}
inline ll rt(ll n){
    int ret=sqrt((double)n+0.5);
    return ret;
}
inline ll ns(ll n){
    ll root=rt(n);
    if(root*root==n) return n;
    root++;
    return root*root;
}


#define sz 10000000
int main(){
    int* roots=new int[sz];
    roots[0]=0;
    roots[1]=1;
    for(int i=2;i<sz;i++){
        if(fair((ll)i) and fair((ll)i*(ll)i)){
            roots[i]=roots[i-1]+1;
        }
        else{
            roots[i]=roots[i-1];
        }
    }
    int t,a,b;
    read(t);
    for(int ii=1;ii<=t;ii++){
        read2(a,b);
        a=ns(a);
        printf("Case #%d: %d\n",ii,roots[rt(b)]-roots[rt(a)-1]);
    }
    return 0;
}
