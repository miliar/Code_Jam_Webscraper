#include <iostream>
#include <cstdio>
#include <cmath>
#define MaxN 1050

using namespace std;

int* BIT;

void init()
{
    int x = sqrt(MaxN);
    BIT = new int[x+5];
    for(int i = 0; i <= x; i++)
        BIT[i] = 0;
}

bool isSquare(int n)
{
    int x = sqrt(n);
    return (x*x==n);
}

int array[20];
bool isPalin(int n)
{
    int i = 0;
    while(n)
    {
        array[i] = n%10;
        n/=10;
        i++;
    }
    i--;

    for(int k = 0; k <= i/2; k++)
        if(array[k] != array[i-k])
            return false;
    return true;
}

void update(int index)
{
    int x = sqrt(MaxN);
    for(int i = index; i <= x; i+=(i&-i))
        BIT[i]++;
}

int get(int index)
{
    int ret=0;
    while(index)
    {
        ret+=BIT[index];
        index-=(index&-index);
    }
    return ret;
}

void preprocess()
{
    int x = sqrt(MaxN);
    for(int i = 1; i <= x; i++)
    {
        if(isPalin(i))
        {
            int k = i*i;
            if(isPalin(k))
                update(i);
        }
    }
}

void solve(int t)
{
    int a, b;
    scanf("%d %d", &a, &b);
    int pa=sqrt(a), pb=sqrt(b);
    if(!isSquare(a))
        pa++;
    printf("Case #%d: %d\n", t, get(pb)-get(pa-1));
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    init();
    preprocess();
    int t; scanf("%d", &t); int cnt=0;
    while(t--)
        solve(++cnt);
    return 0;
}
