#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<bitset>
#include<math.h>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
const int N=100010;
const int MAX=151;
const int mod=100000000;
const int MOD1=100000007;
const int MOD2=100000009;
const double EPS=0.00000001;
typedef long long ll;
const ll MOD=1000000009;
const ll INF=10000000010;
typedef double db;
typedef unsigned long long ull;
char s[110];
int bo[110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,t,ca,len,ans;
    scanf("%d", &t);
    for (ca=1;ca<=t;ca++) {
        scanf("%s", s);
        ans=0;len=strlen(s);
        for (i=1;i<=len;i++)
        if (s[i-1]=='+') bo[i]=1;
        else bo[i]=0;
        for (i=len;i;i--)
        if (!bo[i]) {
            ans++;
            for (j=i;j;j--) bo[j]^=1;
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
/*
5
-
-+
+-
+++
--+-
*/




























