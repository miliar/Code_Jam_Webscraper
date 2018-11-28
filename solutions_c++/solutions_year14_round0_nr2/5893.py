#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main(int argc, char const* argv[]){
    int T, TT;
    double c, f, x, w,t;
    scanf("%d", &T);
    for(TT=1;TT<=T;TT++){
        scanf("%lf %lf %lf",&c,&f,&x);
        w=2.0;
        t=0.0;
        while(w <= (f*x-f*c)/c + 1e-6){
            t += c/w;
            w += f;
            //printf("%.10lf %.10lf\n",t,w);
        }
        printf("Case #%d: %.7lf\n",TT,t+x/w);
    }
    return 0;
}

