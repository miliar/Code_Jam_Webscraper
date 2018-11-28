/**
Craig Bester (CyCraig)
Google Code Jam Round 1B (2015)
Problem A
**/

#include <cstdio>
#include <algorithm>
#include <cstring>

unsigned long  n,min;
unsigned long dp[1000000];

unsigned long reverse(unsigned long  a) {
    unsigned long ret = 0;
    while(a>0) {
        ret *= 10;
        ret += a%10;
        a /= 10;
    }
    //printf("Reverse = %lu\n",ret);
    return ret;
}

unsigned long  solve(unsigned long  a,unsigned long  count, bool lookreverse) {
    //printf("Looking at %lu\n",a);
    if(n < 20) return n;
    if(a > n) return n;
    if(count > min) return n;
    if(a == n) {
        min = count;
        //printf("MINIMUM CHANGED TO %lu\n",count);
        return count;
    }
    
    if(dp[a]) {
        if(count < dp[a]) {
            dp[a] = count;
            if(a < 12) {
                return solve(a+1,count+1,true);
            }
            else {
                unsigned long  i = n;
                if(lookreverse) {
                    unsigned long  rev = reverse(a);
                    if(rev > a) i = solve(rev,count+1,false);
                }
                unsigned long  j = solve(a+1,count+1,true);
                return std::min(i,j);
            }
        }
        else return n;
    }
    else {
        dp[a] = count;
        if(a < 12) {
            return solve(a+1,count+1,true);
        }
        else {
            unsigned long  i = n;
            if(lookreverse) {
                unsigned long  rev = reverse(a);
                if(rev > a) i = solve(rev,count+1,false);
            }
            unsigned long  j = solve(a+1,count+1,true);
            return std::min(i,j);
        }
    }
}


int main(void) {
    freopen("A-small-attempt0(1).in", "r", stdin);
    freopen("out", "w", stdout);
    
    int m;
    scanf("%d\n",&m);
    //printf("Cases = %d\n",m);
    for(int c = 1; c <= m; c++){
        memset(&dp,0,sizeof(dp));
        scanf("%d",&n);
        //printf("curr = %lu\n",n);
        min = n;
        printf("Case #%d: %lu\n",c,solve(1,1,false));
    }
    fflush(stdout);
    
    return 0;
}