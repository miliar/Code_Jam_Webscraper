#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h> 
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

const int N=1e6+100;
vector<int> primes;
bool valid[N];
void get(int n) {
    for (int i=2;i<=n;i++) {
        if (valid[i]) primes.push_back(i);
        for (int j=i+i;j<=n;j+=i)
            valid[j]=false;
    }
}
int a[N];
int lim;
bool ok(long long h,int test) {
    long long mul=1;
    long long ret=0;
    for (int i=1;i<=lim;i++) {
        if (a[i])
            ret+=mul;
        ret%=test;
        mul=mul*h%test;
    }
    return ret==0;
}
int ans[N];
int cnt=0;
bool check(long long x,int mod) {
    long long ret=0;
    long long mul=1;
    for (int i=1;i<=lim;i++) {
        if (a[i]) ret+=mul;
        ret%=mod;
        mul=mul*x%mod;
    }
    return ret==0;
}
void dfs(int step) {
    if (cnt>=50) return;
    if (step>lim) {
        int cc=0;
        for (int i=1;i<=lim;i++) {
            if (a[i]) cc++;
        }
        if (cc&1) return;
        bool bb=true;
        for (int i=2;i<=10&&bb;i+=2) {
            long long mul=i;
            bool hehe=false;
            for (int j=3;j<(int)primes.size();j++) {
                int test=primes[j];
                if (ok(mul,test)) {
                    hehe=true;
                    ans[i]=test;
                    break;
                }
            }
            if (!hehe) bb=false;
        }
        if (bb) {
            for (int i=lim;i>=1;i--) {
                printf("%d",a[i]);
            }
            int ck=0;
            for (int i=2;i<=10;i++) {
                if (i&1) ans[i]=2;
                printf(" %d",ans[i]);
                ck+=check(i,ans[i]);
            }
            if (ck!=9) while (1);
            puts("");
            cnt++;
        }
    }
    else if (step==1||step==lim){
        a[step]=1;
        dfs(step+1);
    }
    else {
        a[step]=0;
        dfs(step+1);
        a[step]=1;
        dfs(step+1);
    }
}
int main () {
    // freopen("in","r",stdin);
    freopen("out","w",stdout);
    for (int i=2;i<=10000;i++) valid[i]=true;
    get(10000);
    lim=16;
    puts("Case #1:");
    dfs(1);
    return 0;
}

