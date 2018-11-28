#include <stdio.h>
int main(){
    FILE *fp;
    int t,ri;
    double c,f,x,p,time;
    fp=fopen("2.out","w");
    scanf("%d",&t);
    for (ri=1;ri<=t;ri++){
        scanf("%lf%lf%lf",&c,&f,&x);
        p=2.0;
        time=0.0;
        while (x/p>c/p+x/(p+f)){
              time+=c/p;
              p+=f;
        }
        time+=x/p;
        fprintf(fp,"Case #%d: ",ri);
        fprintf(fp,"%.7lf\n",time);
    }
    fclose(fp);
    return 0;
}
