#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main(){
    freopen("input2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        double c,f,x,ans=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        int n=max(0,(int)ceil(x/c-2/f-1));
        for(int i=0;i<n;i++)ans+=c/(i*f+2);
        ans+=x/(n*f+2);
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
