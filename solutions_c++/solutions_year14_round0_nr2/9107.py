#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int TC;
    cin >> TC;
    int cas= 1;
    while(TC--){
        double farm, current, inc, target;
        cin >> farm >> inc >> target;
        current= 2;

        double ans1, ans2;
        ans2= target/current;
        double prev= 0;

        do{
            ans1= ans2;
            prev += farm/current;
            ans2= prev+target/(current+inc);
            current += inc;
        }while(ans2 < ans1);

        printf("Case #%d: %.7lf\n", cas, ans1);
        cas++;
    }
}

