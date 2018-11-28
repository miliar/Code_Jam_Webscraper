#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;
#define MAXN 600100
#define inf 1000000000
#define mo 1000000007
int t,n,x;
int box[10011];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&t);
    int cac=0;
    while(t--){
        scanf("%d%d",&n,&x);
        for(int i=1;i<=n;i++){
            scanf("%d",&box[i]);
        }
        sort(box+1,box+1+n);
        int ans=0;
        int j=1;
        int now=0;
        for(int i=n;i>=j;i--){
            if(i!=j){
                if(box[i]+box[j]<=x){
                    ans++;
                    j++;
                }
                else{
                    ans++;
                }
            }
            else{
                ans++;
            }
        }
        cac++;
        printf("Case #%d: %d\n",cac,ans);
    }
    return 0;
}
