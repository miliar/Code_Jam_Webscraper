#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;
int D,P[1010];
priority_queue < int,vector<int>,less<int> >Q;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T,ca=1;
    scanf("%d",&T);
    while(T--){
        while(!Q.empty()) Q.pop();
        scanf("%d",&D);
        int ans, maxP = 0;
        for(int i=0; i<D; ++i){
            scanf("%d",&P[i]);
            Q.push(P[i]);
            maxP = max(maxP,P[i]);
            //printf("maxP=%d P=%d\n",maxP,P[i]);
        }
        ans = maxP;
        for(int i=1; i<=maxP; ++i){
            int t = i;
            for(int j=0; j<D; ++j){
                int x = P[j]/i;
                if(P[j]%i) x++;
                x--;
                t+=x;
            }
            ans = min(ans,t);
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
