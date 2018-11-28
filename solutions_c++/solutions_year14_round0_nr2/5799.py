#include <cstdio>
using namespace std;

int main(int argc, char const *argv[]) {
    int T;
    double C,F,X,cr,ct;

    scanf("%d",&T);
    for(int ca=1; ca<=T; ++ca) {
        scanf("%lf%lf%lf",&C,&F,&X);

        ct=0.0;
        cr=2.0;
        for(;;) {
            if ( (X/cr) < ( (C/cr) + (X/(cr+F)) ) ) {
                ct += X/cr;
                break;
            } else {
                ct += C/cr;
                cr += F;
            }
        }
        printf("Case #%d: %.8lf\n",ca,ct);
    }
    return 0;
}
