#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

void test(int testNum)
{
    long double c, f, x;
    long double ans;
    int n;
    
    scanf("%Lf%Lf%Lf", &c, &f, &x);
    ans = 0.0;
    for(n = 0; c * (2.0 + (n + 1) * f) - x * f < 0.0; ++n)
        ans += 1.0 / (2.0 + n * f);
    ans = c * ans + x / (2.0 + n * f);
    
    printf("Case #%d: %.15Lf\n", testNum, ans);
}

int main()
{
    assert(freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/B/B/B-large.in", "r", stdin) != NULL);
    assert(freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/B/B/output.txt", "w", stdout) != NULL);
    int t, testn;
    scanf("%d", &testn);
    for(t = 1; t <= testn; ++t)
        test(t);
    return 0;
}

