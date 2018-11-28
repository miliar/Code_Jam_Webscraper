#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int a,b,c,i,j,k;
    double N1[1010],N2[1010];
    scanf("%d",&a);
    for(k=1;k<=a;k++){
        printf("Case #%d: ",k);
        scanf("%d",&b);
        for(i=0;i<b;i++){
            scanf("%lf",&N1[i]);
        }
        for(i=0;i<b;i++){
            scanf("%lf",&N2[i]);
        }
        int S=0,E=b-1;
        int cnt1=0,cnt2=0;
        sort(N1,N1+b);
        sort(N2,N2+b);
        for(i=b-1;i>=0;i--){
            if(N2[i]>N1[E]){
                S++;
            }
            else{
                E--;
                cnt1++;
            }
        }
        S=0;
        E=b-1;
        for(i=b-1;i>=0;i--){
            if(N1[i]>N2[E]){
                S++;
                cnt2++;
            }
            else{
                E--;
            }
        }
        printf("%d %d\n",cnt1,cnt2);
    }
    return 0;
}
