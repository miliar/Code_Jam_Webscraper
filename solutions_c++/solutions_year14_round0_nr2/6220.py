#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<map>
#include<vector>
#include<stack>
#include<deque>
#include<list>
#include <algorithm>
#include<iostream>
#include<utility>

using namespace std;
typedef long long LL;




int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int t;
    double c,f,x;
    scanf("%d",&t);
    int T=1;
    while(T++<=t){
        scanf("%lf%lf%lf",&c,&f,&x);
        double res=x/2;
        double q=0,a=2.0;
        for(int g=0;;g++){
            q+=c/(2.0+g*f);
            a+=f;
            if(q+x/a<res)
                res=q+x/a;
            else
                break;
        }
        printf("Case #%d: %f\n",T-1,res);
    }
    return 0;
}
