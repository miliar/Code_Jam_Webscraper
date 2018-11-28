#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double time = 0., ans = X / 2.;
        for(int farm=0; farm<X; ++farm){
            ans = min(ans, X / (2. + F * farm) + time);
            time += C / (2. + F * farm);
        }
        printf("Case #%d: %.7f\n", t, ans);
    }
    return 0;
}
