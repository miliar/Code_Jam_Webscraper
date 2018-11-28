#include <iostream>
#include <cstdio>
#include <cstring>
#define maxn 1010
using namespace std;
double c,f,x;
int t;
int main (){
   // freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int Case=1;Case<=t;++Case){
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans =0.0;
        double speed=2.0;
        while(1){
            if((x/speed)>(c/speed)+(x/(speed+f))){
                ans+=c/speed;
                speed+=f;
            }
            else {
                ans+=x/speed;
                break;
            }
        }
        printf("Case #%d: %.7f\n",Case,ans);
    }
}
