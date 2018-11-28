#include <cstdio>
#include <iostream>
using namespace std;
int main(){
    int ans[4];
    int lans[4];
    int t,n,nc,ncc;
    int _ = 0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("aout.out","w",stdout);
    cin >> t;
    while(t--){
        printf("Case #%d: ",++_);
        nc = 0;ncc = 0;
        int temp;
        scanf("%d",&n);
        n --;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d",&temp);
                if(i == n){
                    ans[nc++] = temp;
                }
            }
        }
        scanf("%d",&n);
        n--;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d",&temp);
                if(i == n){
                    for(int p = 0; p < 4; p++){
                        if(ans[p] == temp){
                            lans[ncc++] = temp;
                        }
                    }
                }
            }
        }
        if(ncc == 1)printf("%d\n",lans[0]);
        else if(ncc == 0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
}
