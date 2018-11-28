#include<stdio.h>
#include<algorithm>
using namespace std;
const int MAXN = 1000 + 10;
main(){
    int T,Case=0,n;
    int cnt1,cnt2;
    double a[MAXN],b[MAXN];
    double tmpa[MAXN],tmpb[MAXN];
    scanf("%d",&T);
    while(T--){
        cnt1=cnt2=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%lf",a+i);
        for(int i=0;i<n;i++)scanf("%lf",b+i);
        sort(a,a+n);
        sort(b,b+n);
        int ia=0,ib=0;
        while(ia<n&&ib<n){
            if(a[ia]>b[ib])ib++,cnt1++;
            else ia++,ib++;
        }
        ia=0,ib=n-1;
        while(ia<n&&ib>=0){
            int iia=ia,iib=0,tot=0;
            while(iia<n&&iib<=ib){
                if(a[iia]>b[iib])iia++,iib++,tot++;
                else break;
            }
            if(tot==ib+1){
                cnt2=tot;
                break;
            }
            if(a[ia]<b[ib]){
                ia++,ib--;
            }
            else{
                cnt2=ib+1;
                break;
            }
        }
        printf("Case #%d: %d %d\n",++Case,cnt2,cnt1);
    }
}
