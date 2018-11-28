#include<stdio.h>
#include<algorithm>
#define N 1010
using namespace std;
double a[N],b[N];
int main(){
    freopen("input2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int n,y=0,z=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)scanf("%lf",a+i);
        for(int i=1;i<=n;i++)scanf("%lf",b+i);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        for(int i=n,j=n;i>=1&&j>=0;i--,j--){
            while(j>=1&&a[i]<b[j])j--;
            if(!j)break;
            y++;
        }
        for(int i=1,j=1;i<=n&&j<=n;i++,j++){
            while(j<=n&&a[i]>b[j])j++,z++;
        }
        printf("Case #%d: %d %d\n",t,y,z);
    }
    return 0;
}
