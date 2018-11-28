#include <stdio.h>
#include <memory.h>
#include <algorithm>
double a[1010],b[1010];
using namespace std;

int cmp(double a, double b) {
        return a>b;
}
int main() {
        int t,k,i,j;
        scanf("%d",&t);
        for(k=1;k<=t;k++) {
                memset(a,0,sizeof(double)*1010);
                memset(b,0,sizeof(double)*1010);
                int n;
                scanf("%d", &n);
                for(i=0;i<n;i++)
                        scanf("%lf",&a[i]);
                for(i=0;i<n;i++)
                        scanf("%lf",&b[i]);
                sort(a,a+n,cmp);
                sort(b,b+n,cmp);
                int ans1,ans2;
                i=j=0;
                ans1=ans2=0;
                while(i<n&&j<n){
                        while(a[i]<=b[j]&&j<n) j++;
                        if(a[i]>b[j]&&i<n&&j<n){
                                ans1++;
                                i++;
                                j++;
                        }
                }
                i=j=0;
                while(i<n&&j<n){
                        while(b[i]<a[j]&&j<n) j++;
                        if(b[i]>a[j]&&i<n&&j<n){
                                ans2++;
                                i++;
                                j++;
                        }
                }
                ans2 = n-ans2;
                printf("Case #%d: %d %d\n",k,ans1,ans2);
        }
        return 0;
}