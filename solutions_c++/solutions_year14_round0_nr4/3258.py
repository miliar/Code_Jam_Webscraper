#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
double e = 1e-8;
int main()
{
    int t, n, i, j;
    double a[1005],b[1005];
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&t);
    for(int cnt = 1;cnt<=t; cnt++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%lf",a+i);
        }
        for(i=0;i<n;i++){
            scanf("%lf",b+i);
        }
        sort(a,a+n);
        sort(b,b+n);
        int tn = n;
        j = 0;
        for(i=0;i<n;i++){
            for(;j<n;j++){
                if(b[j] > a[i]){
                    tn--;
                    j++;
                    break;
                }
            }
        }
        int fn = n;
        j = 0;
        for(i=0;i<n;i++){
            if(a[i] < b[j]){
                fn--;
            }else{
                j++;
            }
        }
        /*j = 0;
        for(i=0;i<n-1;i++)
            a[i] = a[i+1] - e;
        for(i=0;i<n;i++){
            for(;j<n;j++){
                if(b[j] > a[i]){
                    fn--;
                    j++;
                    break;
                }
            }
        }*/
        printf("Case #%d: %d %d\n",cnt, fn, tn);

    }
    return 0;
}
