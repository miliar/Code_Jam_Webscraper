#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
double s1[1010],s2[1010];
bool cmp(double a,double b){
    return a>b;
}
int main(){
    freopen("d1.in","r",stdin);
    freopen("d1.out","w",stdout);
    int t,n,ans1,ans2;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        ans1=0;ans2=0;
        scanf("%d",&n);
        for(int j=0;j<n;j++)
            scanf("%lf",&s1[j]);
        for(int j=0;j<n;j++)
            scanf("%lf",&s2[j]);
        sort(s1,s1+n,cmp);
        sort(s2,s2+n,cmp);
        int k=0;
        for(int j=0;j<n;j++){
            while(k<n){
                if(s1[j]>s2[k]){
                    ans1++;
                    k++;
                    break;
                }
                k++;
            }
        }
        k=0;
        for(int j=0;j<n;j++){
            while(k<n){
                if(s2[j]>s1[k]){
                    ans2++;
                    k++;
                    break;
                }
                k++;
            }
        }
        printf("Case #%d: %d %d\n",i,ans1,n-ans2);
    }
    return 0;
}
