#include <iostream>
#include <cstdio>

using namespace std;

const int N = 1005;
int a[N];

int sort_up(int a[], int n)
{
    int res = 0;
    for(int i = 0; i <= n + 2; i++)
        for(int j = 0; j < n - 1; j++)
            if(a[j] > a[j + 1])
            {
                swap(a[j], a[j + 1]);
                res++;
            }
    return res;
}

int sort_down(int a[], int n)
{
    int res = 0;
    for(int i = 0; i <= n + 2; i++)
        for(int j = 0; j < n - 1; j++)
            if(a[j] < a[j + 1])
            {
                swap(a[j], a[j + 1]);
                res++;
            }
    return res;
}

int bubble_up(int a[], int n)
{
    int res = 0;
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            if(a[i] > a[j]) res++;
    return res;
}

int bubble_down(int a[], int n)
{
    int res = 0;
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            if(a[i] < a[j]) res++;
    return res;
}

int abs(int x) { return x < 0 ? -x : x; }

bool tol[N];
int b[N], cc[N];
int brute(int a[], int n)
{
    int res = 1 << 30;
    for(int i = 0; i < n; i++) b[i] = a[i];
    for(int m = 0; m < (1 << n); m++)
    {
        for(int i = 0; i < n; i++) a[i] = b[i];
        int cnt = 0;
        for(int i = 0; i < n; i++) tol[i] = (m & (1 << i)) != 0;
        int dest = 0;
        for(int i = 0; i < n; i++)
            if(tol[i])
            {
                for(int j = i; j > dest; j--) { swap(a[j], a[j - 1]); cnt++; }
                dest++;
            }
        cnt += sort_up(a, dest);
        cnt += sort_down(a + dest, n - dest);
        if(cnt < res) for(int i = 0; i < n; i++) cc[i] = a[i];
        res = min(res, cnt);
    }
       for(int i = 0; i < n; i++) a[i] = b[i];
    return res;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    //freopen("test.log", "w", stderr);

    int test;
    scanf("%i", &test);

    for(int t = 0; t < test; t++)
    {
        int n;
        scanf("%i", &n);
        for(int i = 0; i < n; i++)
            scanf("%i", &a[i]);
        //if(t == 70) for(int i = 0; i < n; i++) printf("%i%c", a[i], n-1==i?'\n':' ');

        int bbest = brute(a, n);

        int m = 0;
        for(int i = 1; i < n; i++)
            if(a[i] > a[m]) m = i;
        for(int i = m; i > 0; i--) swap(a[i], a[i - 1]);

        int best = 1 << 30;
        int right = bubble_down(a + 1, n - 1), left = 0;
        for(int i = 0; i < n; i++)
        {
            //left = bubble_up(a, i); right = bubble_down(a + i + 1, n - i - 1);
          //  printf(" %i %i\n", left, right);
               best = min(best, left + right + abs(m - i));
            swap(a[i], a[i + 1]);
            for(int j = 0; j < i; j++) if(a[j] > a[i]) left++;
            for(int j = i + 2; j < n; j++) if(a[j] > a[i]) right--;

        }

        //int res = bubble_up(a, m) + bubble_down(a + m + 1, n - m - 1);
        printf("Case #%i: %i\n", t + 1, bbest);
        for(int i = 0; i < n; i++) fprintf(stderr, "%i ", cc[i]); fprintf(stderr, "\n\n");
    }
    return 0;
}
