#include <iostream>
#include<stdlib.h>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#define ll long long
using namespace std;
int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,tt;
    ll pt,r,a,b,c,in;
    float n;
    scanf("%d",&t);
    tt=t;
    while(t--){
        scanf("%lld %lld",&r,&pt);
        a=2;    b=(2*r -1);     c=-pt;
        //n=sqrt(b*b - 4*a*c);    n=n-(b);
        //n/=4;
        in=sqrt(b*b - 4*a*c);    in=in-(b);
        in/=4;
        //printf("%lld\n",in);
        printf("Case #%d: %lld\n",tt-t,in);
    }
  return 0;
}
