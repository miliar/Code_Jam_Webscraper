#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>

using namespace std;

/// fix chislo ferm 


void solve(int test_num)
{
    double c, f, x;
    cin >> c >> f >> x;
    double ans = x / 2.0;
    double curt = 0.0, v = 2.0;
    for (int i = 0; i < 200000; i++)
    {
        curt += c / v;
        v += f;
        ans = min(ans, curt + x / v);
    }
    printf("Case #%d: %.10lf\n", test_num + 1, ans);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i);
}