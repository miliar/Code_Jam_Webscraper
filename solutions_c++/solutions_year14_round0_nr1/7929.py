#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cmath>
#include <vector>
using namespace std;
int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);

    int T,Case=1;
    scanf("%d",&T);
    while(T--){
        int N,M;
        scanf("%d",&N);
        int chash[20]={0};
        vector<int>ans;
        ans.clear();
        for(int i=1; i<=4; ++i)
            for(int j=1; j<=4; ++j){
                int x;
                scanf("%d",&x);
                if(i==N){
                    chash[x] = 1;
                }
            }
        scanf("%d",&M);
        for(int i=1; i<=4; ++i)
            for(int j=1; j<=4; ++j){
                int x;
                scanf("%d",&x);
                if(i==M && chash[x]==1){
                    ans.push_back(x);
                }
            }
        if(ans.size()>1){
            printf("Case #%d: Bad magician!\n",Case++);
        }
        else if(ans.size()==0){
            printf("Case #%d: Volunteer cheated!\n",Case++);
        }
        else{
            printf("Case #%d: %d\n",Case++,ans[0]);
        }
        //printf("%d\n",ans.size());

    }
    return 0;
}
