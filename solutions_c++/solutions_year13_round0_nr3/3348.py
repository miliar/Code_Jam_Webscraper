#include <fstream>
#include <cmath>

using namespace std;

int i, nr[10000001];
int t, T;
long long x, A, B, a, b;

bool palindrom(long long x)
{
    bool ok;
    int i;
    int a[20], nr = 0;
    while(x)
    {
        a[++nr] = (int)((long long)x%10);
        x /= 10;
    }
    ok = 1;
    for(i = 1; i <= nr/2; i++) if(a[i] != a[nr-i+1]) ok = 0;
    return ok;
}

int main()
{
    ifstream fi("test.in");
    ofstream fo("test.out");
    for(i = 1; i <= 10000000; i++)
    if(palindrom(i))
    {
        x = (long long)(i*i);
        if(palindrom(x)) nr[i] = nr[i-1] + 1; else nr[i] = nr[i-1];
    } else nr[i] = nr[i-1];
    fi >> t;
    for(T = 1; T <= t; T++)
    {
        fi >> A >> B;
        a = sqrt((long double)A);
        if((long long)a*a == A) a--;
        b = sqrt((long double)B);
        fo << "Case #" << T << ": " << nr[b] - nr[a] << "\n";

    }
    return 0;
}
