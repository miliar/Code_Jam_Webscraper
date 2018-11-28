#include<bits/stdc++.h>
using namespace std;
double r[2], c[2];
double v, x;
int cmp(double a){
    return a<0?-1:a>0;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int T; cin>>T;
    for(int cs=1; cs<=T; cs++){
        int n; cin>>n>>v>>x;
        printf("Case #%d: ",cs);
        if(n==1){
            cin>>r[0]>>c[0];
            if(c[0]!=x){
                puts("IMPOSSIBLE");
            }
            else{
                printf("%.8f\n",v/r[0]);
            }
        }
        else{
            cin>>r[0]>>c[0]>>r[1]>>c[1];
            int p0=cmp(c[0]-x), p1=cmp(c[1]-x);
            if(p0==0&&p1==0){
                printf("%.8f\n",v/(r[0]+r[1]));
            }
            else if(p0==0){
                printf("%.8f\n",v/r[0]);
            }
            else if(p1==0){
                printf("%.8f\n",v/r[1]);
            }
            else if(p0*p1>0){
                puts("IMPOSSIBLE");
            }
            else{
                double g0=abs(c[1]-x)/(abs(c[0]-x)+abs(c[1]-x))*v;
                double g1=abs(c[0]-x)/(abs(c[0]-x)+abs(c[1]-x))*v;
                printf("%.8f\n",max(g0/r[0],g1/r[1]));
            }
        }
    }
    return 0;
}

