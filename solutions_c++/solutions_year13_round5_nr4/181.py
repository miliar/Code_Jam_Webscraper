#include <iostream>

using namespace std;

const int N = (20 + 5);

int tc, n;

double res;

double dyn[1 << 20];

bool check[1 << 20];

char str[N];

void input()
{
    scanf("%s\n", str);
}

double mem(int t)
{
    int i, s;
    double r = 0.0;
    if(check[t])
    {
        return dyn[t];
    }
    
    s = 0;
    for(i = n - 1; 0 <= i && ((t >> i) & 1); i--, s++);
    for(i = 0; i < n; i++)
    {
        s++;
        if(((t >> i) & 1) == 0)
        {
            r += mem(t | (1 << i)) * (double)s / (double)n + (double)n * (double)s / (double)n - (double)(s - 1) * (double)s / 2.0 / (double)n;
            s = 0;
        }
    }
    check[t] = true;
    return dyn[t] = r;
}

void process()
{
    int i, t = 0;
    
    n = (int)strlen(str);
    
    for(i = 0; i < (1 << n); i++)
    {
        dyn[i] = 0.0;
        check[i] = false;
    }
    check[(1 << n) - 1] = true;
    
    for(i = 0; i < n; i++)
    {
        if(str[i] == 'X')
        {
            t |= 1 << i;
        }
    }
    res = mem(t);
}

void output()
{
    printf("Case #%d: %.10lf\n", tc, res);
}

int main()
{
    int t;
    
    freopen("/Users/protos37/Downloads/D-small-attempt1.in.txt", "r", stdin);
    freopen("/Users/protos37/Downloads/output_.txt", "w", stdout);
    
    scanf("%d", &t);
    
    for(tc = 1; tc <= t; tc++)
    {
        input();
        process();
        output();
    }
    return 0;
}