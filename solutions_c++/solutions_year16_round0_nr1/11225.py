#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;


const int N = 1e6 + 9;
int cot[10];
void toS(int x)
{

    while(x > 0)
    {
        cot[x % 10] ++;
        x /= 10;
    }
}
bool check()
{
    for(int i = 0; i < 10; ++ i)
    {
        if(cot[i] == 0) return 0;
    }
    return 1;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T; scanf("%d", &T);
    int tcas = 1;
    while(T --)
    {
        long long n; cin >> n;
        memset(cot, 0, sizeof(cot));
        long long ans = -1;
        for(int i = 1; i < 1e6; i ++)
        {
            toS(n * i);
            if(check())
            {
                ans = n * i;
                break;
            }
        }
        printf("Case #%d: ", tcas ++);

        if(ans == -1) puts("INSOMNIA");
        else cout << ans << endl;
    }
    return 0;
}







