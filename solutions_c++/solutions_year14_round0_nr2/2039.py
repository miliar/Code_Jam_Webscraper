#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string.h>
#include<cstdlib>

using namespace std;


int main()
{
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\a.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\b.out","w",stdout);
        long long int t, i;
        double c, f, x;
        cin >> t;
        for (i = 1; i <= t; i++){
                cin >> c >> f >> x;
                double a = 2.0;
                double val = x/a;
                double time = 0;
                while (c/a + x/(a+f) < x/a){
                                time += c/a;
                        a = a + f;

                }
                time += x/a;
                printf("Case #%lld: %.7lf\n", i, time);
        }

        return 0;
}
