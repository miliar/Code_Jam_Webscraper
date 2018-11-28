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

int T,n;
bool f[10];
int cnt;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
            memset(f,0,sizeof(f));
            cnt=0;
            scanf("%d",&n);
            for (int i=1;i<=1000;i++){
                    int tmp=n*i;
                    while (tmp!=0){
                            if (!f[tmp%10]){
                                    f[tmp%10]=1;
                                    cnt++;
                            }
                            tmp=tmp/10;
                    }
                    if (cnt==10){
                            printf("Case #%d: %d\n",cas,n*i);
                            break;
                    }
            }
            if (cnt!=10){
                    printf("Case #%d: INSOMNIA\n",cas);
            }
    }
    return 0;
}
