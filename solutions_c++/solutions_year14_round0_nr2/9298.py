#include <stdio.h>
#include <algorithm>

using namespace std;

double pre(double c,double f,double x){
    double aux2,aux=x/2,res;
    double u=2;
    u+=f;
    aux2=(x/u);
    res=(c/2);
    while(aux>res+aux2){
        aux=min(res+aux2,aux);
        aux2=(c/u);
        u+=f;
        res+=aux2;
        aux2=(x/u);
    }
    return aux;
}

int main()
{
    FILE *out;
    out=fopen("out.txt","w");
    FILE *in;
    //in=fopen("in.in","w");
    int t;
    double c,f,x;
    bool check;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%lf %lf %lf",&c,&f,&x);
        double res=pre(c,f,x);
        fprintf(out,"Case #%d: %.7lf\n",i,res);
    }
    fclose(out);
    return 0;
}
