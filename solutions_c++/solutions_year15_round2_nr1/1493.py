#include<cstdio>
#include<queue>
#include<utility>
using namespace std;

#define SIZE 1000006
#define INF 2147483647

typedef pair<int, int> ii;

int D[SIZE];

int reverse_num(int num)
{
    int rev = 0;

    for(; num; num /= 10)
        rev = rev*10+num%10;

    return rev;
}

int SSSP(int u, int v)
{
    int d, rev;
    ii w;
    priority_queue<ii> pQ;

    for(int i = 1; i<SIZE; ++i)
        D[i] = INF;

    D[u] = 0, pQ.push(ii(-D[u], u));
    while(!pQ.empty())
    {
        w = pQ.top(), pQ.pop();
        d = -w.first, u = w.second;
        if(u==v)
            break;

        if(d==D[u])
        {
            if(D[u+1]>d+1)
                D[u+1] = d+1, pQ.push(ii(-D[u+1], u+1));

            rev = reverse_num(u);
            if(D[rev]>d+1)
                D[rev] = d+1, pQ.push(ii(-D[rev], rev));
        }
    }

    return D[v];
}

int solve(int n)
{
    return 1+SSSP(1, n);
}

int main()
{
    int test, t = 1, n;

    for(scanf("%d", &test); t<=test; ++t)
    {
        scanf("%d", &n);
        printf("Case #%d: %d\n", t, solve(n));
    }

    return 0;
}
