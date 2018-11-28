#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int maxn=200;
const double eps=1e-8;
int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    double c,f,x,p,ans;
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%lf%lf%lf",&c,&f,&x);
        p=2.0;
        ans=0.0;
        while(x/p-(x/(p+f)+c/p)>eps){
            ans+=c/p;
            p+=f;
        }
        ans+=x/p;
        printf("Case #%d: %.7f\n",cas,ans);
    }
}
