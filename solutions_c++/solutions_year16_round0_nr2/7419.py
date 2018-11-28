#include<bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FRI freopen("B-small-attempt0.in","r",stdin)
#define FRO freopen("B-small-attempt0.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define EPS 1e-12
#define RAD(x) ((x*PI)/180)
#define MAXN 100005
using namespace std;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

int main() {
    FRI;
    FRO;
    char s[105],prev;
    int T,t=0,n,i,ans;
    scanf("%d",&T);
    while(t++<T) {
        scanf("%s",s);
        prev='+';
        n=strlen(s);
        ans=0;
        for(i=n-1;i>=0;i--) {
            if(s[i]!=prev)
                ans++;
            prev=s[i];
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
