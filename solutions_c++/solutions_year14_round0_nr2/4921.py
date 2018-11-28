#include <cstdio>
#include <queue>
#include <limits.h>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define MAXN 10000
#define INF INT_MAX //nao ha perigo de overflow



double temp(int n,double c, double f, double x){
    double resp = 0;
    double taxa = 2;
    while(n--){
        resp += c/taxa;
        taxa += f;
    }
    return resp+= x/taxa;
}

int minimo(int a, int b, double c, double f, double x){
    if(temp(a,c,f,x)<temp(b,c,f,x)){
        return a;
    }
    return b;
}

int main(){
    int t;
    double c,f,x;
    double min,atual;
    int n,nmax;
    int res;
    scanf("%d", &t);

    for(int i = 0;i<t;i++){
        n = 0;
        nmax = 10000;
        scanf("%lf %lf %lf", &c, &f, &x);
        while(1){
            if(nmax - n == 1){
                res = minimo(n,nmax,c,f,x);
                break;
            }else{
                if(temp((nmax+n)/2, c,f,x)<temp((nmax+n)/2+1,c,f,x)){
                    nmax = (nmax+n)/2;
                }else{
                    n = (nmax+n)/2;
                }
            }
        }

        printf("Case #%d: %.7lf\n",i+1,temp(res,c,f,x));

    }

}