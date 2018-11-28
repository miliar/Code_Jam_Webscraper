#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int maxn = 10000;

bool used[10];

struct Int
{
    int c[maxn], cnt, sz;
    
    Int()
    {
        for (int i = 0; i < maxn; ++i)
            c[i] = 0;
        cnt = sz = 0;
        return;
    }
    Int(int x)
    {
        for (int i = 0; i < maxn; ++i)
            c[i] = 0;
        cnt = sz = 0;
        while (x)
        {
            c[sz++] = x % 10;
            x /= 10;
        }
        return;
    }
    
    void relax()
    {
        for (int i = 0; i < sz; ++i)
        {
            c[i + 1] += c[i] / 10;
            c[i] %= 10;
            used[c[i]] = true;
        }
        while (c[sz])
        {
            c[sz + 1] += c[sz] / 10;
            c[sz] %= 10;
            used[c[sz]] = true;
            ++sz;
        }
    }
    
    void add(int len, int *b)
    {
        sz = max(sz, len);
        for (int i = 0; i < sz; ++i)
            c[i] += b[i];
        
        (*this).relax();
    }
    
    void print()
    {
        for (int i = sz - 1; i >= 0; --i)
            printf("%d", c[i]);
        puts("");
    }
};

bool check()
{
    for (int i = 0; i < 10; ++i)
        if (!used[i]) return false;
    return true;
}

void calc(int testNumber, int x)
{
    if (!x)
    {
        printf("case #%d: INSOMNIA\n", testNumber);
        return;
    }
    Int A(x);
    Int B;
    
    for (int i = 0; i < 10; ++i)
        used[i] = 0;
    
    int cnt = 0;
    
    
    for (int i = 1; ; ++i)
    {
        if (check())
            break;
        B.add(A.sz, &A.c[0]);
        ++cnt;
/*        if (cnt > 100000000)
        {
            printf("case #%d: INSOMNIA\n", testNumber);
            return;
        } */
    }
    
    printf("case #%d: ", testNumber);
    B.print();
    return;
}

int t, x;

int main()
{
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%d", &x);
        calc(i + 1, x);
    }
    return 0;
}