#include <stdio.h>
#include <algorithm>
#define MAX 1005

using namespace std;

double num[MAX],num2[MAX];
double aux[MAX],aux2[MAX];

int pre(int n){
    int cont=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(aux[j]>=aux2[i]){
                aux[j]=-1;
                cont++;
                break;
            }
        }
    }
    return cont;
}

int pre2(int n){
    int cont=0,ptr=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(num2[j]>num[i]){
                num2[j]=-1;
                break;
            }
        }
    }
    for(int i=0;i<n;i++)
        if(num2[i]!=-1)
            cont++;
    return cont;
}

int main()
{
    FILE *out;
    out=fopen("out.txt","w");
    int t,n,cont,res;
    scanf("%d",&t);
    for(int u=1;u<=t;u++){
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&num[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&num2[i]);
        sort(num,num+n);
        sort(num2,num2+n);
        for(int i=0;i<n;i++){
            aux[i]=num[i];
            aux2[i]=num2[i];
        }
        res=pre(n);
        cont=pre2(n);
        fprintf(out,"Case #%d: %d %d\n",u,res,cont);
    }
    fclose(out);
    return 0;
}
