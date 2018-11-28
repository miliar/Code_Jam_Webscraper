#include<cstdio>
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq=1;qq<=tt;qq++) {
        printf("Case #%d: ", qq);
        int n;
        scanf("%d", &n) ;
        vector<int> a(n);
        int maxval=0, minval,sum;
        for(int i=0; i<n; i++) {
            scanf("%d", &a[i]) ;
            maxval=max(maxval,a[i]) ;
        }
        minval=maxval;
        for(int i=1; i<=maxval; i++) {
            sum=i ;
            for(int j=0; j<n; j++) {
                //cout<<sum<<" "<<a[j]<<" "<<" "<<j<<" "<<i<<endl;
                if(a[j]>i) {
                    if(a[j]%i==0 )
                        sum+=(a[j]/i-1) ;
                    else
                        sum+=(a[j]/i) ;
                }
            }
            //cout<<sum<<" "<<minval<<endl;
            minval=min(minval,sum) ;
        }
        printf("%d\n", minval) ;
    }
    return 0;
}
