#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
double eps = 1e-9;
int main()
{
    int t, i, j;
    double r[105], c[105];
    int n;
    double x, v;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int cnt = 1;cnt <= t;cnt++){
        scanf("%d",&n);
        scanf("%lf%lf",&v,&x);
        for(i=0;i<n;i++)
            scanf("%lf%lf",&r[i],&c[i]);
        int aa[105], sn = 0, gn = 0, en = 0;
        for(i=0;i<n;i++){
            if(c[i] < x - eps)
                aa[i] = -1, sn++;
            else if (c[i] > x+ eps)
                aa[i] = 1, gn++;
            else
                aa[i] = 0, en++;
        }
        double vs = 0, vg = 0, ve = 0;
        double xvs = 0, xvg = 0, xve = 0;
        for(i=0;i<n;i++){
            if(aa[i] == -1){
                vs += r[i];
                xvs += c[i]*r[i];
            }else if(aa[i] == 1){
                vg += r[i];
                xvg += c[i]*r[i];
            }else{
                ve += r[i];
                xve += c[i]*r[i];
            }
        }
        if(sn == 0 || gn == 0){
            if(en == 0){
                printf("Case #%d: IMPOSSIBLE\n", cnt);
                continue;
            }else{
                printf("Case #%d: %lf\n",cnt,v/ve);
                continue;
            }
        }
        double xs = xvs/vs, xg = xvg/vg;
        double a = (x - xs)/(xg - x);
        double tn = max(1/vs, a/vg);
        double rr = (1 + a)/tn;
        rr += ve;
        //printf("x:%lf %lf\n",xs,xg);
        //printf("a:%lf\n",a);
        //printf("t:%lf\n",tn);
        printf("Case #%d: %lf\n",cnt,v/rr);
    }
    return 0;
}
