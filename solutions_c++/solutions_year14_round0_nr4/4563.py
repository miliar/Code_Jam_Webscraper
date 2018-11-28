#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T;
int n;
const double eps=1e-9;
double a[1100],b[1100];
int ans1,ans2;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int tt=1;tt<=T;tt++){
        printf("Case #%d: ",tt);
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%lf",&a[i]);
        for (int i=1;i<=n;i++) scanf("%lf",&b[i]);
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        //if (tt==14){
        //    for (int i=1;i<=n;i++) cout<<a[i]<<' ';
        //    cout<<endl;
        //    for (int i=1;i<=n;i++) cout<<b[i]<<' ';
        //    cout<<endl;
        //}
        int t=1,s=1;
        ans1=n;  ans2=0;
        for (int i=1;i<=n;i++){
            while (t<=n&&b[t]<a[i]+eps) t++;
            if (t<=n) {
                ans1--;
                t++;
            }
        }
        t=n;
        for (int i=1;i<=n;i++){
            if (a[i]>b[s]){
                s++; ans2++;
            }
        }
        printf("%d %d\n",ans2,ans1);
    }
}
