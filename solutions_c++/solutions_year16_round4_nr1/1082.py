#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<cassert>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<unordered_map>
#include<queue>
#include<tuple>
using namespace std;
typedef long long int lnt;
typedef unsigned long long int unt;
typedef unsigned ust;
typedef double dou;
typedef pair<int,int> P;
#define FZ(i,n)       for(int i=0;i<(n);++i)
#define FB(i,n)       for(int i=(n)-1;i>=0;--i)
#define FV(i,st,ed)   for(int i{st};i<(ed);++i)
#define FC(i,n)       for(int i{n};i;--i)
#define FZU(i,n)      for(ust i{0};i!=(n);++i)
#define FVU(i,st,ed)  for(ust i{st};i<(ed);++i)
#define FCU(i,n)      for(ust i{n};i;--i)
#define SZ(x)         ((int)x.size())
#define ALL(x)        (x).begin(),(x).end()
#define likely(x)     __builtin_expect(!!(x), 1)
#define unlikely(x)   __builtin_expect(!!(x), 0)

#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define RI64(x) scanf("%I64d",&(x))
#define RII64(x,y) scanf("%I64d%I64d",&(x),&(y))

#define FIR first
#define SEC second
#define pritnf printf
constexpr ust N = 100514u;

int n,r,p,s;
string a[13][3],aa;
void sol(int uuu){
    scanf("%d %d %d %d",&n,&r,&p,&s);
    aa = "Z";
    bool ok = false;
    FZU(i,3){
        if(count(ALL(a[n][i]),'R')==r&&count(ALL(a[n][i]),'P')==p){
            ok = 1;
            aa=min(aa,a[n][i]);
        }
    }
    printf("Case #%d: ",uuu);
    if(ok){
        puts(aa.c_str());
    }else{
        puts("IMPOSSIBLE");
    }
}
int main(){
    a[0][0]="R";
    a[0][1]="P";
    a[0][2]="S";
    FZU(i,12)FZU(j,3){
        for(auto c:a[i][j]){
            if(c=='R')a[i+1][j]+="SR";
            if(c=='P')a[i+1][j]+="RP";
            if(c=='S')a[i+1][j]+="PS";
        }
    }
    FZ(k,13)FZU(l,3){
        int n = k;
        auto&ans = a[k][l];
        FZ(i,n)for(int j=0;j<(1<<n);j+=(1<<(i+1))){
            if(!lexicographical_compare(ans.begin()+j,ans.begin()+j+(1<<i),ans.begin()+j+(1<<i),ans.begin()+j+(1<<(i+1)))){
                swap_ranges(ans.begin()+j,ans.begin()+j+(1<<i),ans.begin()+j+(1<<i));
            }
        }
    }
	freopen("A-large.in","r",stdin);
	freopen("Al.txt","w",stdout);
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++)sol(ti);
	}
	return 0;
}

