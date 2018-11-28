#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;

#define N 1005
#define P 1005
#define INF 1LL<<61
#define LL  long long
#define MOD 1000000007

#define MID ((l + r)/2)
#define lx (x<<1)
#define rx ((x<<1)|1)
int ans;
int p[N];
int n;

int main(){
    //freopen("../in.txt","r",stdin);
    int tt;
    scanf("%d",&tt);
    int mmax;
    for(int cas=1;cas<=tt;cas++){
        mmax = 0;
        ans = 0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&p[i]);
            mmax = max(mmax,p[i]);
        }
        ans = mmax;
        for(int da=1;da<=mmax;da++){
            int total = 0;
            int chuan = 0;
            for(int i=1;i<=n;i++){
                if(p[i] > da){
                    total += p[i]/da;
                    if(p[i]%da==0){
                        total--;
                    }
                    chuan = max(chuan,da);
                }
                else{
                    chuan = max(chuan,p[i]);
                }
            }
            total += chuan;
            ans = min(ans,total);
        }
        printf("Case #%d: %d\n",cas,ans );
    }
    return 0;
}