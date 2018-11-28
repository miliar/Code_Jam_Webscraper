#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<iomanip>
using namespace std;

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define N 100

int a[N][N], b[N][N];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("b.txt", "w", stdout);
    //freopen("a.txt","r",stdin);

    int T;
    cin>>T;
    FOR(kk, 1, T)
    {
        double c, f, x, v, t, s;
        cin>>c>>f>>x;
        s = 2;
        v = 0;
        t = 0;
        if (c >= x)
            t = x / s;
        else
        {
            while (v < x)
            {
                if (v >= c)
                {
                    double tp1, tp2;
                    tp1 = (x - v) / s; /// not buy
                    tp2 = (x - (v - c)) / (s + f); /// buy
                    if (tp1 < tp2)
                    {
                        t += tp1;
                        break;
                    }
                    else
                    {
                        v -= c;
                        s += f;
                    }
                }

                t += (c - v) / s;
                v = c;
            }
        }

        printf("Case #%d: ", kk);
        cout<<setiosflags(ios::fixed);
        cout<<setprecision(7)<<t<<endl;
    }

    //fclose(stdout);
    return 0;
}
