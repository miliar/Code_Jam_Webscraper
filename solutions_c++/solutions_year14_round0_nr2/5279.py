#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

FILE *in = fopen( "B-large.in", "r" );
FILE *out = fopen( "B-large.out", "w" );
int t;
double c,f,x;
int cnt = 0;
void solve() {
    cnt ++;
    fscanf(in,"%lf%lf%lf",&c,&f,&x);

    double ans1 = 0,ans2 = 0;
    int a = (x * f - 2 * c) / f / c;
   // printf("%d\n",a);
    int j;
    //scanf("%d",&ss);
    for(j = 0;j < a;j ++)
        ans1 += c/(2.0 + j * f);
    ans1 += x/(2.0 + j * f);
    //if(a >= 0){
        for(j = 0;j < a + 1;j ++)
            ans2 += c/(2.0 + j * f);
        ans2 += x/(2.0 + j * f);
        if(ans1 > ans2) ans1 = ans2;
   // }
    //printf("ans::%lf \n",ans);
    fprintf(out,"Case #%d: %.7lf\n",cnt,ans1);
}
int main() {
    fscanf(in,"%d",&t);
    while(t --) {
        solve();
    }
    fclose(in);
    fclose(out);
    return 0;
}
