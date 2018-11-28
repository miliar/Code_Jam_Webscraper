#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<string>
#include<bitset>
#define LL long long

const int MAXN=0;
const int MAXM=0;
const long long LLINF=9000000000000000000;
const int INF=2147483647;//careful because of floyed and so on
const int MOD=1000000007;
double eps=0.00000001;

using namespace std;

int T;
int len;
char s[107];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
            scanf("%s",s);
            len=strlen(s);
            int ans=0;
            for (int i=1;i<len;i++){
                    if (s[i]!=s[i-1]){
                            ans++;
                    }
            }
            if (s[len-1]=='-') ans++;
            printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
