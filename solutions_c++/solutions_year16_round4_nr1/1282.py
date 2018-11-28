#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
string calc(int r,int p,int s,int idx) {
    if(r+p+s==2) {
        if(!r)
            return "PS";
        if(!p)
            return "RS";
        return "PR";
    }
    string a,b;
    if((r+p+s)%3==1) {
        if(idx==1) {
            a=calc(r>>1,p>>1,s+1>>1,2);
            b=calc(r>>1,p+1>>1,s>>1,3);
        } else if(idx==2) {
            a=calc(r>>1,p>>1,s+1>>1,1);
            b=calc(r+1>>1,p>>1,s>>1,3);
        } else {
            a=calc(r>>1,p+1>>1,s>>1,1);
            b=calc(r+1>>1,p>>1,s>>1,2);
        }
    } else if(idx==1) {
        a=calc(r>>1,p>>1,s+1>>1,3);
        b=calc(r>>1,p+1>>1,s>>1,2);
    } else if(idx==2) {
        a=calc(r>>1,p>>1,s+1>>1,3);
        b=calc(r+1>>1,p>>1,s>>1,1);
    } else {
        a=calc(r>>1,p+1>>1,s>>1,2);
        b=calc(r+1>>1,p>>1,s>>1,1);
    }
    return a<b?a+b:b+a;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,r,p,s;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%d%d%d%d",&n,&r,&p,&s);
        printf("Case #%d: ",cas);
        if(min(min(r,p),s)+1<max(max(r,p),s))
            puts("IMPOSSIBLE");
        else if(r==p)
            puts(calc(r,p,s,3).c_str());
        else if(p==s)
            puts(calc(r,p,s,1).c_str());
        else
            puts(calc(r,p,s,2).c_str());
    }
    return 0;
}
