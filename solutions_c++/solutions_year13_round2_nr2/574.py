#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

typedef long long i64;

int n, x, y;

i64 C[22][6];
void Init()
{
    C[0][0] = 1;
    for(int i=1; i<=20; i++)
	{
        C[i][0] = 1;
        for(int j=1; j<=6 && j<=i; j++)
            C[i][j] = (C[i-1][j] + C[i-1][j-1]);
    }
}
int a[100];
int main()
{
    freopen("C:\\codejam\\B-small-attempt0.in", "r", stdin);
    freopen("C:\\codejam\\B-small-attempt2.out", "w", stdout);
    Init();
    int out = 1;
    int T;
    scanf("%d", &T);
    a[1]=1;
    a[2]=6;
    a[3]=15;
    while(T--){
        scanf("%d%d%d", &n, &x, &y);
        if(x < 0) x = -x;
        printf("Case #%d: ", out++);
        if((x+y)&1) {
            printf("0.0\n");
        }

        else {
        for(int i=1;i<=3;i++)
            if(a[i]>=(x+y)){
            if(x+y <= 4) printf("1.0\n");
            else
            {
                int t = n - a[i];
                if(x+y > i*2 || y+1 > t) printf("0.0\n");
                else
                {
                    if(y+1 <= 6)
                    {
                        double ans = 0;
                        if(t>=6+y+1) ans = 1.0;
                        else
                        {
                            int cc = 6;
                            while(t > cc) {
                                t-=2;
                                --y;
                                --cc;
                            }
                            for(int i=y+1; i<=t; i++)
                                ans += C[t][i]*pow(0.5, t);
                        }
                        printf("%.8f\n", ans);
                    }
                    else printf("0.0\n");
                }
            }
        }
        }
    }

    return 0;
}
