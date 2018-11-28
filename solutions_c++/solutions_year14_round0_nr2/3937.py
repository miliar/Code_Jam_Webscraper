#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    scanf("%d",&N);
    double C,F,X;
    for(int i=0;i<N;i++){
        scanf("%lf %lf %lf",&C,&F,&X);
        double N=X/2,A=1000000,VelPro=2,time=0,TT=0;
        while(N<A){
            A=N;
            time=C/VelPro;
            VelPro+=F;
            N=X/VelPro+TT+time;
            TT+=time;
        }
        printf("Case #%d: %.7lf\n",i+1,A);
    }
    fclose(stdout);
}
