#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cot = 1;
    int T;scanf("%d", &T);
    while(T --)
    {
        double C, F, X;
        cin >> C >> F >> X;

        double ans = 0, S = 2, cntX = 0;
        while(1)
        {
            if(X > (C + S * C / F))
            {
//                X -= C;
                ans += C / S;
                S += F;
            }
            else
            {
                ans += X / S;
                break;
            }
        }
        printf("Case #%d: ", cot ++);
        printf("%.7f\n", ans);
    }
    return 0;
}







