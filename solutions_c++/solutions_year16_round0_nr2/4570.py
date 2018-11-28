// Author : Muhammad Rifayat Samee
// Problem : B
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
char str[105];
int memo[105][2];
int done[105][2],cc=1;

int n;

int dp(int i,int f){
    if(i == n){
        if(f == 1)return 0;
        return 1;
    }
    if(done[i][f] == cc)
        return memo[i][f];
    int res = INF;
    int cur;
    if(str[i] == '-')cur = 0;
    else
        cur = 1;
    if(i == 0){
        res=min(res,dp(i+1,cur));
        res = min(res,dp(i+1,!cur)+1);
    }
    else{
        if(f == cur)res = min(res,dp(i+1,f));
        else{
            if(cur==0){
                res = min(res,dp(i+1,1)+2);
                res = min(res,dp(i+1,0)+1);
            }
            else{
                res = min(res,dp(i+1,1)+1);
                res = min(res,dp(i+1,0)+2);
            }
        }
    }
    memo[i][f] = res;
    done[i][f] = cc;
    return res;

}

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
    int cases,i,j,k,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%s",str);
        n = strlen(str);
        printf("Case #%d: %d\n",ct++,dp(0,0));
        cc++;
    }
	return 0;
}
