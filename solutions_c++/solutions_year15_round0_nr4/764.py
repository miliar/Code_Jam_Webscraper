#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
    //freopen("D-large.in","r",stdin);
    //freopen("D-large.out","w",stdout);
    int t,x,r,c,k=0;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d%d",&x,&r,&c);
        bool ans=1;
        if(x>6)
            ans = 0;
        else if(x>r&&x>c)
            ans = 0;
        else if((r*c)%x)
            ans = 0;
        else if((x+1)/2>min(r,c))
            ans = 0;
        else if(x<4)
            ans = 1;
        else if(x==4)
            ans = min(r,c)>2;
        else if(x==5)
            ans = !(min(r,c)==3&&max(r,c)==5);
        else if(x==6)
            ans = min(r,c)>3;
        printf("Case #%d: %s\n",++k,ans?"GABRIEL":"RICHARD");
    }

}
