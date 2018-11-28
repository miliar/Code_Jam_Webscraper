#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;
#define DPF(fmt,...) printf(fmt,##__VA_ARGS__); fprintf(outf, fmt,##__VA_ARGS__);
const int MAX_STR = 2000;
#define RI(val) int val = 0; scanf("%d", &val);
#define RULL(val) unsigned long long val = 0; scanf("%llu", &val);
#define RF(val) float val = 0.0f; scanf("%f", &val);
#define RS(val) string val; {char str[MAX_STR]; scanf("%s", str); val = str;}
#define RC(val) char val = 0; scanf("%c", &val);
#define RL(val) string val; {char str[MAX_STR]; fgets(str, MAX_STR - 1, stdin); int len = strlen(str); if (str[len - 1] == '\n'){str[len - 1] = '\0';}else{str[len] = '\0';} val = str;}
#define RNL() {char str[MAX_STR]; fgets(str, MAX_STR, stdin);}
#define REP(ii, nn) for (int ii = 0; ii < nn; ii++)
typedef unsigned long long ULL;
typedef long long LL;

ULL powerof2[45];

int main()
{
    FILE* stdi = stdin;
    FILE* inf = freopen("in.txt", "r", stdin);
    FILE* outf = fopen("out.txt", "w");

    ULL s = 1;
    REP(i, 45)
    {
        powerof2[i] = s;
        s *= 2;
    }
    RI(np); RNL();
    for (int pp = 1; pp <= np; pp++)
    {
        DPF("Case #%d: ", pp);
        RULL(P); RC(c); RULL(Q); RNL();

        bool possible = false;
        int g = 0;

        //reduce fraction
        if (Q % P == 0)
        {
            Q /= P;
            P /= P;
        }

        int div = -1;
        REP(i, 40)
        {
            if (powerof2[i] % Q == 0)
            {
                div = i;
                break;
            }
        }

        if (div >= 0)
        {
            ULL factor = powerof2[div] / Q;
            P *= factor;
            Q *= factor;

            // assume previous generation was 0/1 and something.  count generations
            while (possible == false)
            {
                P = 2 * P;
                g++;

                if (P >= Q)
                {
                    possible = true;
                    break;
                }

            }
        }

        if (possible)
        {
            DPF("%d\n", g);
        }
        else
        {
            DPF("impossible\n");
        }

    }
    fclose(inf);
    fclose(outf);
    return 0;
}