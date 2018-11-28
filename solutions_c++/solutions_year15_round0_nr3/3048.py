#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
map<PII,int> M;
int l,x,now;
char s[10005];
int main() {
    M.clear();
    M[make_pair(1,1)] = 1;
    M[make_pair(1,2)] = 2;
    M[make_pair(1,3)] = 3;
    M[make_pair(1,4)] = 4;
    M[make_pair(2,1)] = 2;
    M[make_pair(2,2)] = -1;
    M[make_pair(2,3)] = 4;
    M[make_pair(2,4)] = -3;
    M[make_pair(3,1)] = 3;
    M[make_pair(3,2)] = -4;
    M[make_pair(3,3)] = -1;
    M[make_pair(3,4)] = 2;
    M[make_pair(4,1)] = 4;
    M[make_pair(4,2)] = 3;
    M[make_pair(4,3)] = -2;
    M[make_pair(4,4)] = -1;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca = 0;
    while (T--) {
        printf("Case #%d: ",++ca);
        scanf("%d%d",&l,&x);
        scanf("%s",s);
        int ans = 1;
        for (int i = 0; i<l; i++) {
            if (s[i] == 'i') now = 2;
            if (s[i] == 'j') now = 3;
            if (s[i] == 'k') now = 4;
            ans = (ans*now>0?1:-1)*(M[make_pair(abs(ans),abs(now))]);
        }
        if (!((x%2==0 && x%4!=0 && abs(ans)!=1) || (x%2==1 && ans==-1))) {puts("NO"); continue;}

        int ed;
        int ei;
        ed = min(4,x)*l;
        ans = 1;
        for (ei = 0; ei<ed; ei++) {
            if (s[ei%l] == 'i') now = 2;
            if (s[ei%l] == 'j') now = 3;
            if (s[ei%l] == 'k') now = 4;
            ans = (ans*now>0?1:-1)*(M[make_pair(abs(ans),abs(now))]);
            if (ans == 2) break;
        }
        if (ei == ed) {puts("NO"); continue;}

        int lk;
        ans = 1;
        for (lk = l*x-1; lk>=l*x-ed; lk--) {
            if (s[lk%l] == 'i') now = 2;
            if (s[lk%l] == 'j') now = 3;
            if (s[lk%l] == 'k') now = 4;
            ans = (ans*now>0?1:-1)*(M[make_pair(abs(now),abs(ans))]);
            //printf("%d %d ",lk,l*x-ed);
            if (ans == 4) break;
        }
        if (lk == l*x-ed-1) {puts("NO"); continue;}
        //printf("%d %d ",ei,lk);
        if (ei+1<lk) puts("YES");
              else puts("NO");
    }
}
