#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#define f first
#define s second
using namespace std;
typedef pair<double,double> par;
par ar[105];
int main(){
    int T,t=0;
    scanf("%d",&T);
    while(T--){t++;
        int n;
        double v,x;
        scanf("%d%lf%lf",&n,&v,&x);
        for(int i=0;i<n;i++)
            scanf("%lf%lf",&ar[i].s,&ar[i].f);
        printf("Case #%d: ",t);
        sort(ar,ar+n);
        if(ar[0].f>x||ar[n-1].f<x){
            puts("IMPOSSIBLE");
            continue;
            }
        if(n==1){
            printf("%.10f\n",v/ar[0].s);
            continue;
            }
        else if(n==2){
            if(ar[0].f==x&&ar[1].f==x)
                printf("%.10f\n",v/(ar[0].s+ar[1].s));
            else if(ar[0].f==x)
                printf("%.10f\n",v/(ar[0].s));
            else if(ar[1].f==x)
                printf("%.10f\n",v/(ar[1].s));
            else
            printf("%.10f\n",max(v*(x-ar[0].f)/((x-ar[0].f)+(ar[1].f-x))/ar[1].s,v*(ar[1].f-x)/((x-ar[0].f)+(ar[1].f-x))/ar[0].s));
            continue;
            }
        else{
            puts("Error");
            }
        }
    return 0;
    }
