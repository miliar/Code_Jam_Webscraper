#include <iostream>
#include<stdio.h>
using namespace std;

struct element {double prob; int conf;};
element vda[(1<<17)+3];
int ms, ii, t, k, sol[20], n, K, mr, mc, sol1[20];
double v[20], x[20], prob,nrsol,  maxim, prob1da, prob1nu, prob2da, prob2nu, probeg,vnu[1<<20], sum;


void gen1(int poz, double prob){
    if (poz==k+1){
        mr=ms-mc;
        if ((mc&mr)==0){
            double prob2=1;
            for(int i=1;i<=n;i++)
                if (mr&(1<<i))
                    prob2=prob2*(1-v[i]);
            nrsol++;
            sum+=(prob*prob2);//+(1-prob)*(1-prob2))  /   ((prob*prob2+(1-prob)*(1-prob2))+(1-prob)*prob2+(prob)*(1-prob2));
        }
    }else{
        for (int i=sol1[poz-1]+1;i<=2*k;i++){
            sol1[poz]=i;
            mc+=1<<sol[i];
            gen1(poz+1,prob*v[sol[i]]);
            mc-=1<<sol[i];
        }
    }
}

void gen(int poz){
    if (poz==2*k+1){
        mc=0;sum=nrsol=0;
        gen1(1,1);
        if (sum>maxim)
            maxim=sum;
    }else{
        for (int i=sol[poz-1]+1;i<=n;i++){
            sol[poz]=i;
            ms+=(1<<i);
            gen(poz+1);
            ms-=(1<<i);
        }
    }
}
int main()
{
   // freopen("a.in","r",stdin);
  //  freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int iii=1;iii<=t;iii++){
        scanf("%d %d",&n,&K);
        for (int i=1;i<=n;i++){
            scanf("%lf",&v[i]);
            x[i]=v[i]*10;
        }
        k=K/2;
        prob=1;
        nrsol=0;
        maxim=0;
        gen(1);
       /* maxim=0;
        double p10=0;
        for (int i=1;i<=k;i++)
            p10=p10*10;
        for (int i=1;i<=nrsol;i++)
            for (int j=1;j<=nrsol;j++)
                if ((vda[i].conf&vda[j].conf)==0){
                    prob1da=vda[i].prob;    prob1nu=(vnu[i]);
                    prob2da=vda[j].prob;    prob2nu=(vnu[j]);
                    probeg=((prob1da*prob2nu)+(prob1nu*prob2da)) / ((prob1da*prob2nu)+(prob1nu*prob2da)+(prob1da*prob2da)+(prob1nu*prob2nu));
                    if (probeg>maxim)
                        maxim=probeg;
                }
        /*/
        printf("Case #%d: %f\n",iii,maxim);//?????
    }
    return 0;
}
