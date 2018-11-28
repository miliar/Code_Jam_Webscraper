#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int T;
double C,F,X;

int main(void){

    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    scanf("%d",&T);

    for(int caso=1;caso<=T;caso++){
        printf("Case #%d: ",caso);


        scanf("%lf %lf %lf",&C,&F,&X);

        double resp=X/2;

        double tot=0;
        double rate=2;
        while(tot<=resp){
            resp=min(resp,tot+X/rate);
            tot+=C/rate;
            rate+=F;
        }

        printf("%.7lf\n",resp);

    }

    return 0;
}
