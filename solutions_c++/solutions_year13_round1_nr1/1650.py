#include<cstdio>
#include<cmath>
#define PI 3.14159254
using namespace std;
int T, r, t;
double tt;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d", &T);
    for (int i = 0; i < T; i++){
        scanf("%d%d",&r,&t);
        tt = (double)t;

        int num=0, ct=0;
        while (tt > 0){
              if (num&1){
                 tt -= (2*(r+num)-1);
                 if ((tt > 0)||(abs(tt) < 1e-9)){ct++;}
              }
              num++;
        }
        printf("Case #%d: %d\n",i+1,ct);
    }
    return 0;
}

