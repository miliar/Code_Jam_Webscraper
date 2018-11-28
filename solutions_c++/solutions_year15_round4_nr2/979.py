#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n,m;
double v,x;
double r[3],c[3];

int dcmp(double x){
    if(x<-1e-9)return -1;
    if(x>1e-9)return 1;
    return 0;
}
void input(){
    scanf("%d%lf%lf",&n,&v,&x);
    for(int i=0; i<n; i++)
        scanf("%lf%lf",&r[i],&c[i]);
}

void solve(){
    static int cas=1;
    printf("Case #%d: ",cas++);
    if(n==2 && dcmp(c[0]-c[1])==0){
        n=1;
        r[0]+= r[1];
    }
    if(n==1){
        if(dcmp(c[0]-x)==0){
            printf("%f\n",v/r[0]);
        }else{
            printf("IMPOSSIBLE\n");
        }
        return;
    }
    if      (dcmp(c[0]-x)==0){
        printf("%f\n",v/r[0]);
    }else if(dcmp(c[1]-x)==0){
        printf("%f\n",v/r[1]);
    }else if(dcmp(c[0]-x)*dcmp(c[1]-x)==-1){
        printf("%f\n", max((x-c[1])*v/(c[0]-c[1])/r[0] ,(x-c[0])*v/(c[1]-c[0])/r[1]));
    }else{
        printf("IMPOSSIBLE\n");
    }
}

int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    int zz;
    scanf("%d",&zz);
    while(zz--){
        input();
        solve();
    }
    return 0;
}

/*
2 12.5848 53.3212
23.6753 53.3212
22.5766 53.3212
*/
