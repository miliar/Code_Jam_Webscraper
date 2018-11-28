#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
using namespace std;
#define pb push_back
#define mp make_pair
#define For(i, n) for(int i = 0; i < (n); i++)
#define ForD(i, n) for(int i = (n) - 1; i >= 0; i--)
typedef long long LL;

const int N = 11000;
char A[N] = {};
char Calc[N][N];
bool Minus[N][N];

pair<char, bool> mult(char l, char r)
{
    if (l == '1')
        return mp(r, false);
    if (r == '1')
        return mp(l, false);
    if (l == r)
        return mp('1', true);
    
    if (l == 'i' and r == 'j')
        return mp('k', false);
    
    if (l == 'j' and r == 'i')
        return mp('k', true);
    
    if (l == 'i' and r == 'k')
        return mp('j', true);
    
    if (l == 'k' and r == 'i')
        return mp('j', false);
    
    if (l == 'j' and r == 'k')
        return mp('i', false);
    
    if (l == 'k' and r == 'j')
        return mp('i', true);
    
    return mp('x', false);
}

inline pair<char, bool> mult(int l, int r)
{
    return mp(Calc[l][r], Minus[l][r]);
}

bool checkOK(int l, int r, int n)
{
    if (abs(l - r) < 2)
        return false;
    
    auto left = mult(0, l);
    auto mid = mult(l + 1, r - 1);
    auto right = mult(r, n - 1);
    
    if (left.second or mid.second or right.second)
        return false;
    if (left.first != 'i' or mid.first != 'j' or right.first != 'k')
        return false;
    
    return true;
}

void Prepare(int n)
{
    For (i, n)
        for (int j = i; j < n; j++)
        {
            if (i == j)
                Calc[i][j] = A[i];
            else
            {
                auto res = mult(Calc[i][j - 1], A[j]);
                Calc[i][j] = res.first;
                Minus[i][j] = res.second ^ Minus[i][j - 1];
            }
        }
}

int main()
{
    int t;
    scanf("%d", &t);
    
    For (k, t)
    {
        int L, X;
        scanf("%d %d", &L, &X);
        
        For (i, L)
            scanf(" %c", &A[i]);
        For (i, X - 1)
            For (j, L)
                A[j + L * (i + 1)] = A[j];
        
        int n = L * X;
        
        Prepare(n);
        
        bool ok = false;
        For (i, n)
            for (int j = i + 1; j < n; j++)
                if (checkOK(i, j, n))
                {
                    ok = true;
                    goto end;
                }
    end:
        if (ok)
            printf("Case #%d: YES\n", k + 1);
        else
            printf("Case #%d: NO\n", k + 1);
    }
}