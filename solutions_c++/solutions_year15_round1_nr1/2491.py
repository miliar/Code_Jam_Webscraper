#include <cstdio>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
long long n,mi[10009],t,i,j,z,rate,ii,cmax,y,x;
int main(){
    freopen("MushroomLarge.in","r",stdin);
	freopen("MushroomLarge.out","w",stdout);
    scanf("%lld",&t);
    for (x=1; x<=t; x++){
        z=0; y=0;
        scanf("%lld",&n);
        for (i=0; i<n; i++){
            scanf("%lld",&mi[i]);
        }
        cmax=mi[0];
        rate=0;
        for (i=0; i<n-1; i++){
            rate=max(rate,mi[i]-mi[i+1]);
        }
        for (i=0; i<n-1; i++){
            z=z+min(rate,mi[i]);
        }
        for (i=1; i<n; i++){
            if (mi[i]>cmax){
                cmax=mi[i];
            }
            else if (mi[i]<cmax){
                y=y+cmax-mi[i];
                cmax=mi[i];
            }
        }
        printf("Case #%lld: %lld %lld\n",x,y,z);
    }
}
