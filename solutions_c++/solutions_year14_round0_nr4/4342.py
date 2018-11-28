#include <cstdio>
#include<algorithm>
using namespace std;
double A[1010],B[1010];
int main()
{
//    freopen("D-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%lf",&A[i]);
        for(int i=1;i<=n;i++) scanf("%lf",&B[i]);
        sort(A+1,A+1+n);
        sort(B+1,B+1+n);
        int war=0;
        for(int i=1,j=1;j<=n;)
        {
            if(A[i]<B[j]) {i++;j++;war++;}
            else j++;
        }
        war=n-war;
        int dwar=0;
        for(int i=1,j=1;i<=n&&j<=n;)
        {
            if(A[i]>B[j]) {i++;j++;dwar++;}
            else {i++;}
        }
        printf("Case #%d: %d %d\n",kase,dwar,war);

////        for(int i=1;i<=n;i++) printf("%lf ",A[i]);
////        puts("");
////        for(int i=1;i<=n;i++) printf("%lf ",B[i]);
////        puts("");


    }
    return 0;
}
