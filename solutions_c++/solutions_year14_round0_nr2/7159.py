#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        double c,f,x,v=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=x/v,s=0;
        for(int i=1;s<ans;i++){
            s+=c/v;
            v+=f;
            ans=min(ans,s+x/v);
        }
        printf("Case #%d: %.15f\n",++no,ans);
    }
}
