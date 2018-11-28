#include <iostream>
#include<cstdio>
#include<cstring>

using namespace std;
double cntime(double C,double F,int  i){
    if(i==1) return C/2.0;
    else return C/(2+(i-1)*F)+cntime(C,F,i-1);
}

int main()
{
    freopen("B-small-attempt5.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=1;
    double C,F,X;
    while(t<=T){
        scanf("%lf%lf%lf",&C,&F,&X);
        getchar();
        double tim,mint=X/2,time1,time2;
        for(int i=1;i*C<X;i++){
            time1=X/(i*F+2);
            time2=cntime(C,F,i);
            tim=time1+time2;
            if(tim<mint) mint=tim;
            else break;
            //cout << time1 << "  "<< time2 << endl;
        }
        printf("Case #%d: %.7lf\n",t,mint);
        t++;
    }
    return 0;
}
