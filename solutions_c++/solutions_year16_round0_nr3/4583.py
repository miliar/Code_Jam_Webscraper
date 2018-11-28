#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

#define I64 long long int
#define INF 0x7f7f7f7f
#define SIZE 1000
#define MAX 2000
#define EPS 1e-9
#define PI 2*acos(0.0)

#define PII pair <int, int>
#define PLL pair <I64, I64>
#define PDD pair <double, double>
#define PSI pair <string, int>
#define PIS pair <int, string>
#define PSS pair <string string>

#define MII map <int, int>
#define MLL map <I64, I64>
#define MDD map <double, double>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string string>

#define VI vector <int>
#define VS vector <string>
#define QI queue <int>
#define QS queue <string>
#define SI stack <int>
#define SS stack <string>

#define pb push_back
#define pob pop_back
#define mp make_pair

#define IT iterator
#define ff first
#define ss second

#define SET(a, b) memset( a, b, sizeof (a) )
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define IAMHERE cout << "YES\n";
#define DEBUG(a, b) cout << a << ": " << b << "\n";

I64 bases[12][35];
I64 ans[12];

void setBases (void)
{
    for (int i = 2; i < 11; i++) {
        bases[i][0] = 1;
        for (int j = 1; j <= 16; j++) {
            bases[i][j] = i * bases[i][j-1];
        }
    }

//    for (int i = 2; i < 11; i++) {
//        for (int j = 0; j <= 16; j++) {
//            cout << bases[i][j] << " ";
//        }
//        cout << endl;
//    }
    return;
}

I64 findDiv (I64 num)
{   //I64 n = num;
    for (I64 i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return num / i;
        }
    }
    //DEBUG("Return Prime", n);
    return -1;
}

bool anyPrime(int mask)
{
    vector <int> pos;
    //DEBUG ("mask", mask);
    for (int i = 0; i <= 16; i++) {
        if (mask & (1 << i)) {
            pos.push_back(i);
        }
    }
    //for (int i = 0; i < pos.size(); i++) cout << pos[i] << " ";cout << endl;

    for (int base = 2; base <= 10; base++) {
        I64 sum = 0;
        for (int i = 0; i < pos.size(); i++) {
            sum += bases[base][pos[i]];
        }
        I64 div = findDiv(sum);//DEBUG("sum", sum);
        if (div == -1) return true;
        else ans[base] = div;
    }
    return false;
}

void Print (int mask, int n)
{
    int bits[n+5]; //DEBUG("mask", mask);
    for (int i = 0; mask > 0; i++) {
        bits[i] = mask % 2;
        mask = mask >> 1;
    }
    //reverse(bits, bits+n+1);
    for (int i = n-1; i >= 0; i--) {
        printf("%d", bits[i]);
    }

    for (int i = 2; i <= 10; i++) {
        printf(" %lld", ans[i]);
    }
    puts("");
    return;
}

int main()
{
    READ("C-small-attempt2.in");
    WRITE("out.txt");
    int Case=1;
    int n, j;
    char dump[2];

    setBases();

    int tc; scanf("%d", &tc);

    while (tc--) {
        scanf("%d %d", &n, &j);

        int N = (1 << (n-1)) + 1;
        int counter = 0;

        printf("Case #%d:\n", Case++);

        for (int mask = N; counter < j; mask++) {
            if ((mask & 1) && (mask & (1 << (n-1)))) {
                if (!anyPrime(mask)) {
                    counter++;
                    Print(mask, n);
                }
            }
        }
    }
    return 0;
}
