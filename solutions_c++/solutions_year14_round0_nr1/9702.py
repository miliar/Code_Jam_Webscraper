#include <cstdio>
using namespace std;
 
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
 
    int i,j,t,ans,n,b1[4],b2[4],cnt,c;
 
    scanf("%d",&t);
    c = t;
    while(t--){
        scanf("%d",&ans);
        for(i=0; i<4; i++){
            for(j=0; j<4; j++){
                scanf("%d", &n);
                if (ans-1 == i){ b1[j] = n; }
            }
        }
        scanf("%d",&ans);
        for(i=0; i<4; i++){
            for(j=0; j<4; j++){
                scanf("%d", &n);
                if (ans-1 == i){ b2[j] = n; }
            }
        }
        cnt = 0;
        for(i=0; i<4; i++){
            for(j=0; j<4; j++){
                if(b1[i] == b2[j]){ cnt++; ans = b1[i]; }
            }
        }
        printf("Case #%d: ", c-t);
        if (cnt > 1){ printf("Bad magician!\n"); }
        else if (cnt){ printf("%d\n", ans); }
        else { printf("Volunteer cheated!\n"); }
    }
}
