#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
double a1[2000], a2[2000];
bool cmp(double a, double b) {
    return a > b;
}
int main() {
    freopen("war2.in","r",stdin);
    freopen("war.out","w",stdout);
    int tc, n, test = 1;
    scanf("%d",&tc);
    while (tc--) {
        scanf("%d",&n);
        for (int i=0; i<n; i++) {
            scanf("%lf",&a1[i]);
        }
        for (int i=0; i<n; i++) {
            scanf("%lf",&a2[i]);
        }
        sort(a1, a1+n);
        sort(a2, a2+n);
        //deceitful
        int cnt1 = 0, p1 = n-1, p2 = n-1;
        while (p2 >= 0) {
            //cout<<" p1 : "<<p1<<"  p2 : "<<p2<<"   a[p1] : "<<a1[p1]<<"   a2[p2] : "<<a2[p2]<<endl;
            if (a1[p1] > a2[p2]) {
                p1--;   p2--;
                cnt1 += 1;
            } else {
                p2--;
            }
            //cout<<"cnt1 : "<<cnt1<<endl;
        }
        //war
        int cnt2 = 0;
        p1 = n-1, p2 = n-1;
        while (p1 >= 0) {
            //cout<<" p1 : "<<p1<<"  p2 : "<<p2<<"   a[p1] : "<<a1[p1]<<"   a2[p2] : "<<a2[p2]<<endl;
            if (a1[p1] < a2[p2]) {
                p1--;   p2--;
            } else {
                cnt2 += 1;
                p1--;
            }
            //cout<<"cnt2 : "<<cnt2<<endl;
        }
        printf("Case #%d: %d %d\n",test,cnt1,cnt2);
        test += 1;
    }
    return 0;
}
