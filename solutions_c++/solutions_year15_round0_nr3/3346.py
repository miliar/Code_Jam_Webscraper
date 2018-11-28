#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int mat[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int dp[10005][10005];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,i,j,L,X,cs=1, sgn, val;
    string s,ts;
    cin>>t;
    while(t--){
        cin>>L>>X>>ts;
        s = "";
        for(i = 0;i<X;i++){
            s+=ts;
        }
        L = L*X;
        for(i = 0;i<L;i++){
            dp[i][i] = s[i]-'i'+2;
            for(j = i+1;j<L;j++){
                    if(dp[i][j-1]<0)
                        sgn = -1;
                    else sgn = 1;
                    val = sgn*dp[i][j-1];
                    dp[i][j] = sgn*mat[val][s[j]-'i'+2];
            }
        }
        for(i = 0;i<L-2;i++){
            if(dp[0][i] != 2) continue;
            for(j = i+2;j<L;j++){
                if(dp[j][L-1] != 4) continue;
                if(dp[i+1][j-1]!=3) continue;
                break;
            }
            if(j<L)
                break;
        }
        printf("Case #%d: %s\n",cs++,(L>2 && i<L-2?"YES":"NO"));
    }
	return 0;
}
