#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <algorithm>
//psyduck
#define ll long long
#define S(x) scanf("%d",&x)
#define Sf(x) scanf("%f",&x)
#define Slf(x) scanf("%lf",&x)
#define Sl(x) scanf("%lld",&x)
#define P(x)  printf("%d\n", x)
#define Pf(x)  printf("%f\n", x)
#define Plf(x)  printf("%lf\n", x)
#define Pl(x)  printf("%lld\n", x)
using namespace std;
#include <iostream>
#include <cstdio>

int main()
{

     FILE *fi, *fo;
    int t,z,i,n,ans,count;
    fi = fopen("inp.txt", "r");
    fo = fopen("op.txt", "w");
    char s[1005];
    int a[10005];
    fscanf(fi,"%d", &t);
    for (z = 1; z <= t; z++){
    fscanf(fi,"%d", &n);
    fscanf(fi,"%s", s);
    for (i = 0; i <= n; i++){
        a[i] = s[i]-48;
    }
    /*for (i = 0; i <= n; i++){
        fprintf(fo,"%d\n",a[i]);
    }*/
    count = a[0];
    ans = 0;
    //cout << count;
    //fprintf(fo,"%d\n",count);
    for (i = 1; i <= n; i++){
        if(count >= i){
            count = count + a[i];
        }
        else {
            ans = ans+1;
            count = count + a[i]+1;
        }
        //cout << count;
    }
    fprintf(fo,"Case #%d: %d\n",z,ans);
    //cout << ans;
    }
    return 0;
}
