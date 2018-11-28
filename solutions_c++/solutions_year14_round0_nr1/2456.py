#include<algorithm>
#include<vector>
#include<stdio.h>
#include<set>
#include<map>

using namespace std;
int T,a,x,ind;
map<int,int> h;
int main(){
    freopen("codejam.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        ++ind;
        h.clear();
        for(int k=0;k<2;++k){
        scanf("%d",&a);
            for(int i=1;i<=4;++i){
                for(int j=1;j<=4;++j){
                    scanf("%d",&x);
                    if(i==a){
                        h[x]++;
                    }
                }
            }
        }
        int nr=0,ret;
        for(int i=1;i<=16;++i){
            if(h[i]==2){
                //printf("%d ",i);
                ++nr;
                ret=i;
            }
        }
        printf("Case #%d: ",ind);
        if(nr == 1){
            printf("%d",ret);
        }else if(nr>=2){
            printf("Bad magician!");
        }
        else{
            printf("Volunteer cheated!");
        }
        printf("\n");
    }
}
