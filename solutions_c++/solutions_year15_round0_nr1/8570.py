#include <bits/stdc++.h>
using namespace std;

int main(){
    int z;
    scanf("%d",&z);
    for(int j=1;j<=z;j++){
        int maxS;
        scanf("%d ",&maxS);
        int res = 0,stand = 0;
        for(int i = 0;i<=maxS;i++){
            if(i>stand){
                stand++;
                res++;
            }
            char a;
            scanf("%c",&a);
            stand += (a-'0');
        }
        printf("Case #%d: %d\n",j,res);
    }
    return 0;
}
