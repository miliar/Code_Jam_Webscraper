#include<cstdio>

using namespace std;
int main(){
    int t,i;
    double c,f,x,res,total;
    scanf("%d", &t);
    for (i = 0; i < t; i++){
        scanf("%lf%lf%lf", &c, &f, &x);
        res = 2.0;
        total = 0.0;
        while (c/res + x/(res+f) < x/res){
            total += c/res;
            res += f;
        }
        total += x/res;
        printf("Case #%d: %.7lf\n", i+1, total);
    }
}
