//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007

int tcase;
double c,f,x;
double rek(double cps){
    if (((x-c)/cps)<(x/(cps+f)))return x/cps;
    return c/cps+rek(cps+f);
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&tcase);
    for (int i=1;i<=tcase;i++){
        cin >> c >> f >> x;
        if (x<=c){
            printf("Case #%d: %.7lf\n",i,x/2.0);
        }
        else{
            double res=0.0;
            double cps=2.0;
            while(((x-c)/cps)>(x/(cps+f))){
                res+=(c/cps);
                cps+=f;
            }
            res+=(x)/cps;
            printf("Case #%d: %.7lf\n",i,res);
 
        }
    }
    return 0;
}
