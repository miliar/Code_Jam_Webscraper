// Google Code Jam 2016
// Qualifying Round

#include <cstdio>
#include <vector>

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

using namespace std;

int N, T;
vector<int> V;

void Mark(int n)
{
    if (n == 0)
    {
        ++V[0];
    }
    else
    {
        while (n > 0)
        {
            ++V[n % 10];
            n /= 10;
        }
    }
}

bool Asleep()
{
    for (int i = 0; i <= 9; ++i)
        if (V[i] == 0)
            return false;
            
    return true;
}

void Solve()
{
    V.clear();
    V.resize(10, 0);
    
    for (int step = 1; step <= 100; ++step)
    {
        int now = N * step;
        
        Mark(now);
        
        if (Asleep())
        {
            printf("%d\n", now);
            return;
        }
    }
    printf("INSOMNIA\n");
}

int main()
{
    freopen(INPUT_FILE, "rt", stdin);
    freopen(OUTPUT_FILE, "wt", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        scanf("%d", &N);
        printf("Case #%d: ", i);
        Solve();
    }
   
   return 0;
}

