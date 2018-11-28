#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

#define sf scanf
#define pf printf
#define LLU unsigned long long
#define Lu unsigned long
#define LLD long long
#define LD long
#define fo(i, n) for(i = 0; i < n; i++)
#define fa(i, n) for(i = 0; i < n - 1; i++)
#define oof(i, n) for(i = n - 1; i >= 0; i--)
#define max 100000000000000+1

void input();
void save_sqr();
void save_res();
void save_finalres();
bool cheak_palindrom(long long n);

vector <long long> sqr;
vector <long long> res;
vector <long long> fres;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    save_sqr();
    save_res();
    save_finalres();
    input();

    return 0;
}
void save_sqr()
{
    LLD i = 1, tmp = 1;
    while(tmp < max)
    {
        tmp = i * i;
        sqr.push_back(tmp);
        i++;
    }
}
void save_res()
{
    LLD i, n = sqr.size(), tmp;
    bool ck;
    fo(i, n)
    {
        ck = false;
        tmp = sqr[i];
        ck = cheak_palindrom(tmp);
        if(ck) res.push_back(tmp);
    }
}
void save_finalres()
{
    LLD i, n = res.size(), tmp;
    bool ck;
    fo(i, n)
    {
        ck = false;
        tmp = sqrt(res[i]);
        if(tmp * tmp == res[i])
        {
            ck = cheak_palindrom(tmp);
            if(ck) fres.push_back(res[i]);
        }
    }
}
bool cheak_palindrom(long long n)
{
    LLD i, len, tmp, j;
    char in[16];
    memset(in, 0, 16);
    i = 0;
    while(n != 0)
    {
        tmp = n % 10;
        in[i++] = tmp + 48;
        n /= 10;
    }

    len = i / 2;
    j = i - 1;
    fo(i, len)
    {
        if(in[i] != in[j]) return false;
        j--;
    }
    return true;
}
void input()
{
    LLD kag = 0, a, b, i, T, j, cou, len = fres.size();
    sf("%lld", &T);
    while(T--)
    {
        cou = 0;
        sf("%lld%lld", &a, &b);
        fo(i, len)
        {
            if(fres[i] > b) break;
            if(fres[i] >= a && fres[i] <= b) cou++;
        }
        pf("Case #%lld: %lld\n", ++kag, cou);
    }
}

