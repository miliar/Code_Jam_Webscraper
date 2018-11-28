//  test
//  File.cpp
/*
    ID: Firwaless
    LANG: C++
    TASK: 
*/

#include <cstdio>

int main()
{
    //freopen("/Users/firwaless/Downloads/B-large.in.txt", "r", stdin);
    //freopen("/Users/firwaless/Downloads/B-large.out.txt", "w", stdout);
    
    int t, T;
    double c, f, x, g, ans;
    
    scanf("%i", &T);
    for (t = 1; t <= T; ++t) {
        ans = 0.;
        g = 2.;
        scanf("%lf%lf%lf", &c, &f, &x);
        while (x / g > c / g + x / (g + f)) {
            ans += c / g;
            g += f;
        }
        printf("Case #%i: %.7lf\n", t, ans + x / g);
    }
    return 0;
}