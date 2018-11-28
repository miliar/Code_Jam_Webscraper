#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int T,R,C,W;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        scanf("%d %d %d",&R,&C,&W);
        int ans=(C/W)*R+W;
        if(C%W)
            ;
        else
            ans--;
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
