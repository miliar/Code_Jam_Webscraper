#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("aa.in","r",stdin);
    freopen("aa.out","w",stdout);
    int cases, caseno=0, n, m1, m2, mx, i, a[1100];

    scanf("%d", &cases);
    while(cases--){
        scanf("%d", &n);
        mx = m1 = m2 = 0;
        for(i=0; i<n; i++)
        {
            scanf("%d", &a[i]);
            if(i>=1 && mx<a[i-1]-a[i])
                mx = a[i-1]-a[i];
        }
        for(i=0; i<n; i++)
        {
            if(i>=1 && a[i-1]-a[i]>0)
                m1 += a[i-1]-a[i];
            if(i+1<n){
                if(a[i]<mx)
                    m2 += a[i];
                else
                    m2 += mx;
            }
        }
        printf("Case #%d: %d %d\n", ++caseno, m1, m2);
    }

    return 0;
}

