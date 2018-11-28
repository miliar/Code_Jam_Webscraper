#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <climits>
#include <map>

using namespace std;

double fun(double c,double f,double x,double speed)
{
    if(x/speed < c/speed + x/(speed+f))
        return x/speed;
    else
        return c/speed + fun(c,f,x,speed+f);
}

int main() {
    freopen("/Users/l/Documents/codejam/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/l/Documents/codejam/B-small-attempt0.out.txt", "w", stdout);
    int T,out = 1;
    double c,x,f;
    cin>>T;
    //printf("%d\n",T);
    //return 0;
    while (T--) {
        printf("Case #%d: ",out++);
        cin>>c>>f>>x;
        double ans = fun(c,f,x,2);
        printf("%.7lf\n",ans+1e-9);
    }
    return 0;
}