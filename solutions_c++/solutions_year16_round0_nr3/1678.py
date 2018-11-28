//priority_queue
#pragma comment(linker, "/STACK:102400000,102400000")
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <iostream>
#include <algorithm>
#include <functional>
#include <assert.h>
using namespace std;
#define IOS std::ios::sync_with_stdio (false);std::cin.tie(0)
#define pb push_back
#define PB pop_back
#define bk back()
#define fs first
#define se second
#define sq(x) ((x)*(x))
#define eps (1e-8)
#define INF (0x3f3f3f3f)
#define clr(x) memset((x),0,sizeof (x))
#define cp(a,b) memcpy((a),(b),sizeof (b))

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

#define chl (o<<1)
#define chr ((o<<1)|1)
#define mi ((l+r)>>1)


const int maxn=32;
struct Node{
    int a[40];
    bool operator < (const Node &C)const{
        for(int i=0;i<maxn;i++){
            if(a[i]>C.a[i]) return 0;
            else if(a[i]<C.a[i]) return 1;
        }
        return 0;
    }
};
set<Node> hash;
const int maxp=8;
ll p[10]={2,3,5,7,11,13,17,23};
ll pm[12][10][40];
void init(){
    for(int base=2;base<=10;base++){
        for(int i=0;i<maxp;i++){
            pm[base][i][0]=1;
        }
    }
    for(int base=2;base<=10;base++){
        for(int i=0;i<maxp;i++){
            for(int f=1;f<maxn;f++){
                pm[base][i][f]=pm[base][i][f-1]*base%p[i];
            }
        }
    }
}
int a[40];
void getrand(){
    a[0]=1,a[maxn-1]=1;
    for(int i=1;i<maxn-1;i++){
        a[i]=rand()%2;
    }
}
int testBase(int b){
    for(int pr=0;pr<maxp;pr++){
        int pp=p[pr];
        ll tmp=0;
        for(int i=0;i<maxn;i++){
            tmp=(tmp+a[i]*pm[b][pr][i]%pp)%pp;
        }
        if(tmp==0) return pp;
    }
    return 0;
}
int ds[2000];
Node tmp;
int main(){
    ////freopen("/home/slyfc/CppFiles/in","r",stdin);
    freopen("/home/cwind/CppFiles/out","w",stdout);
    puts("Case #1:");
    srand(2343);
    init();
    int cnt=0;
    for(;cnt<500;){
        getrand();
        bool f=1;
        for(int b=2;b<=10;b++){
            if(!(ds[b]=testBase(b))){
                f=0;
                break;
            }
        }
        if(f){
            memcpy(tmp.a,a,sizeof a);
            if(hash.find(tmp)!=hash.end()) continue;
            hash.insert(tmp);
            cnt++;
            for(int i=maxn-1;i>=0;i--) printf("%d",a[i]);
            for(int i=2;i<=10;i++) printf(" %d",ds[i]);
            puts("");
        }
    }
    return 0;
}
