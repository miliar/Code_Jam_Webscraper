#include<algorithm>
#include<vector>
#include<stdio.h>
#include<set>
#include<map>

using namespace std;
int T,a,x,ind;
map<int,int> h;
double C,F,X,R,best = 10101010.0,TIME;
int main(){
    freopen("codejam.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    while(T--){
       R=2;
       ++ind;
       best = 10101010.0;
       TIME = 0;
       int ext=0;
       scanf("%lf%lf%lf",&C,&F,&X);
       while(true){
            if(best < (X / R + TIME)){
                ++ext;
            }else{
                best = X/R + TIME;
            }
            if(ext == 10)
                break;
            TIME += C/R;
            R += F;
            //printf("%lf ",TIME);
       }
       printf("Case #%d: %.10lf\n",ind,best);
    }
}
