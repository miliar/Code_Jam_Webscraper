#include<cstdio>
#include<cstring>
int a[20][20];
double c,f,x;
const double eps=1e-7;
bool check(double tot){
    double rate=2,sum=0,tmp;
    while(tot>eps){
        if(tot*rate>x)return 1;
        tmp=c/rate;
     //   printf("tot=%lf rate=%lf\n",tot,rate);getchar();
        if((tot-tmp)*f>c-eps){
            tot-=tmp;
            rate+=f;
        }
        else
        break;
    }
    return tot*rate>x;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,n,m,cs,csi;
    double l,r,mid;
    scanf("%d",&cs);
    for(csi=1;csi<=cs;csi++){
        scanf("%lf%lf%lf",&c,&f,&x);
        l=0;r=x/2;
        while(l<r-eps){
            mid=(l+r)/2;
            if(check(mid))r=mid;
            else l=mid;
        }
        printf("Case #%d: ",csi);
        printf("%.9lf\n",r);
    }
    return 0;
}

