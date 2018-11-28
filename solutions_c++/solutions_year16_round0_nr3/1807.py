#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <algorithm>
#include <ctime>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned int uint;
#ifdef _DEBUG
#define DPF(fmt,...) { printf(fmt,##__VA_ARGS__); fprintf(outf, fmt,##__VA_ARGS__); }
#else
#define DPF(fmt,...) { fprintf(outf, fmt,##__VA_ARGS__); }
#endif
const int MAX_STR = 100000;
#define RI(val) int val = 0; scanf("%d", &val);
#define RIS(val, nn) vector<int> val; { for (int ii = 0; ii < (nn); ii++) { int vval; scanf("%d", &vval); val.push_back(vval); } }
#define RLL(val) LL val = 0; scanf("%lld", &val);
#define RLLS(val, nn) vector<LL> val; { for (int ii = 0; ii < (nn); ii++) { LL vval; scanf("%lld", &vval); val.push_back(vval); } }
#define RD(val) double val = 0.0f; scanf("%lf", &val);
#define RDS(val, nn) vector<double> val; { for (int ii = 0; ii < (nn); ii++) { double vval; scanf("%lf", &vval); val.push_back(vval); } }
#define RC(val) char val = 0; scanf("%c", &val);
#define RS(val) string val; {char str[MAX_STR]; scanf("%s", str); val = str;}
#define RL(val) string val; {char str[MAX_STR]; fgets(str, MAX_STR - 1, stdin); int len = strlen(str); if (str[len - 1] == '\n'){str[len - 1] = '\0';}else{str[len] = '\0';} val = str;}
#define RNL() {char str[MAX_STR]; fgets(str, MAX_STR, stdin);}
#define REP(ii, nn) for (int ii = 0; ii < (nn); ii++)
#define REPS(ii, mm, nn) for (int ii = (mm); ii < (nn); ii++)
#define swap(a, b) {auto t = a; a = b; b = t;}

int jamcoin[11];
LL orig[11];

int basen(uint val, int base, LL& orig)
{
    LL start = 1;
    uint v = val;
    LL basev = 0;
    while(v)
    {
        if (v & 1)
        {
            basev += start;
        }
        start *= (LL)base;
        v >>= 1;
    }

    orig = basev;

    if (basev % 2 == 0)
    {
        return 2;
    }

    LL i = 3;
    while(i * i <= basev)
    {
        if (basev % i == 0)
        {
            return (int)i;
        }
        i += 2;
    }

    return -1;
}

int main()
{
    FILE* inf = freopen("in.txt", "r", stdin); FILE* outf = fopen("out.txt", "w");
    RI(np); RNL();
    for (int pp = 1; pp <= np; pp++)
    {
#ifndef _DEBUG
        printf("Case #%d\n", pp);
#endif
        DPF("Case #%d:\n", pp);

        RI(N); RI(J);
        int numcoins = 0;
        int val = 1 + (unsigned int)pow(2, N - 1);
        while(numcoins < J)
        {
            memset(jamcoin, 0, sizeof(jamcoin));
            memset(orig, 0, sizeof(orig));
            bool found = true;
            REPS(i, 2, 11)
            {
                jamcoin[i] = basen(val, i, orig[i]);
                if (jamcoin[i] == -1)
                {
                    found = false;
                    break;
                }
            }
            if (found)
            {
                int v = val;
                string s = "";
                while(v)
                {
                    s.push_back((v % 2) ? '1' : '0');
                    v /= 2;
                }
                int sz = s.size();
                for (int i = sz - 1; i >= 0; i--)
                {
                    DPF("%c", s[i]);
                }
                REPS(i, 2, 11)
                {
                    DPF(" %d", jamcoin[i]);
                    //DPF(" %d (%d)", jamcoin[i], orig[i]);
                }
                DPF("\n");
                numcoins++;
            }
            // jamcoins have to be odd
            val += 2;
        }

    }
    fclose(inf);
    fclose(outf);
    return 0;
}