#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;
#define MAXN 1005
#define inf 1000000000
#define mo 1000000007
int t,n;
int box[1011];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&t);
    int cac=0;
    int o=0;
    while(t--){
        cac++;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&box[i]);
        }
        int l=1,r=n;
        int ans=0;
        while(l<r){
            int minn=inf;int bj;
            for(int i=l;i<=r;i++){
                if(minn>box[i]){
                    minn=box[i];
                    bj=i;
                }
            }
            if(bj-l<r-bj){
                for(int i=bj;i>l;i--){
                    box[i]=box[i-1];
                }
                ans+=bj-l;
                l++;
            }
            else{
                for(int i=bj;i<r;i++){
                    box[i]=box[i+1];
                }
                ans+=r-bj;
                r--;
            }
        }
        printf("Case #%d: %d\n",cac,ans);
    }
    return 0;
}
