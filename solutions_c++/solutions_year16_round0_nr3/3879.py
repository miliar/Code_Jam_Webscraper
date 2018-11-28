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
int n,m;
LL now=0;
int ans[13];

int main(){
    freopen("c_small.out","w",stdout);
    scanf("%d",&T);
    scanf("%d%d",&n,&m);
    printf("Case #1:\n");
    now=1;
    now=now<<(n-1);
    now=now|1;
    for (int i=1;i<=m;i++){
            while (1){
                    bool flag=1;
                    for (int j=2;j<=10;j++){
                            LL tmp=1;
                            LL res=0;
                            for (int k=0;k<n;k++){
                                    if ((now>>k)&1) res=res+tmp;
                                    tmp=tmp*j;
                            }
                            //printf("%d %I64d\n",j,res);
                            ans[j]=-1;
                            for (LL i=2;i*i<=res;i++){
                                    //printf("%I64d %I64d\n",res,i);
                                    if (res%i==0){
                                            ans[j]=i;
                                            break;
                                    }
                            }
                            if (ans[j]==-1){
                                    flag=0;
                                    break;
                            }
                    }
                    if (flag==1){
                            for (int i=n-1;i>=0;i--) printf("%I64d",(now>>i)&1);
                            for (int i=2;i<=10;i++) printf(" %d",ans[i]);
                            printf("\n");
                            now+=2;
                            break;
                    }
                    now+=2;
            }
    }
    return 0;
}
