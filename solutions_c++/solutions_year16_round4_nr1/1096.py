/*
-----------------------------------------------------------------------------
Author :            ---------------------------------------------------------
    UTKAR$H $AXENA  ---------------------------------------------------------
    IIT INDORE      ---------------------------------------------------------
-----------------------------------------------------------------------------
*/
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define fre 	freopen("0.in","r",stdin);freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
#define LL signed long long int
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define rep(i,from,to) for(int i=(from);i <= (to); ++i)
#define pii pair<int,int>

struct S {
    int r,s,p;
    S() {}
    S(int x,int y,int z) {
        r=x;
        s=y;
        p=z;
    }
    S add(S x) {
        return S(x.r+r,x.s+s,x.p+p);
    }
    bool equal(int x,int y,int z) {
        return x==r and y==s and z==p;
    }
} dp[23][4];
void pre_calc() {
    int N = 13;
    dp[1][1] = S(1,0,0);
    dp[1][2] = S(0,1,0);
    dp[1][3] = S(0,0,1);
    for(int i=2; i<=N; ++i) {
        dp[i][1] = dp[i-1][1].add(dp[i-1][2]);
        dp[i][2] = dp[i-1][2].add(dp[i-1][3]);
        dp[i][3] = dp[i-1][3].add(dp[i-1][1]);
    }
}
string  printResult(int i,int N) {
    if(N==1) {
        string C;
        if(i==1)C="R";
        if(i==2)C="S";
        if(i==3)C="P";
        return C;
    } else {
        if(i==1) {
            string x = printResult(2,N-1);
            string y = printResult(1,N-1);

            return min(x+y,y+x);
        }
        if(i==2) {
            string x = printResult(3,N-1);
            string y = printResult(2,N-1);

            return min(x+y,y+x);
        }
        if(i==3) {
            string x = printResult(3,N-1);
            string y = printResult(1,N-1);

            return min(x+y,y+x);
        }
    }
}
int main() {
    fre;
    pre_calc();
    int T,r,p,s,N;
    cin>>T;
    rep(t,1,T) {
       cin>>N>>r>>p>>s;
        printf("Case #%d: ",t);
        string ans = "Z";
        if(dp[N+1][3].equal(r,s,p)) {
            ans=min(ans,printResult(3,N+1));
        }
        if(dp[N+1][1].equal(r,s,p)) {
            ans=min(ans,printResult(1,N+1));
        }
        if(dp[N+1][2].equal(r,s,p)) {
            ans=min(ans,printResult(2,N+1));
        }
        if(ans=="Z") {
            cout<<"IMPOSSIBLE\n";
        } else {
            cout<<ans<<endl;
        }
    }
}
