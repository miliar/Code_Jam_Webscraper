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
#define MAX 110
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

int pos[MAX];

int main()
{
    READ("B-large.in");
    WRITE("out.txt");
    int Case=1;
    char dump[2];
    string s;

    int tc; scanf("%d", &tc);
    gets(dump);

    while (tc--) {
        getline(cin, s);

        string happy;
        int idx = 0;

        for (int i = 0; i < s.size(); i++) {
            happy += '+';
        }

        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] != s[i + 1]) {
                pos[idx++] = i;
            }
        }

        for (int i = 0; i < idx; i++) {
            reverse(s.begin(), s.begin() + pos[i] + 1);
            for (int j = 0; j <= pos[i]; j++) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        //cout << idx << "->" << happy;
        if (s != happy) idx++;
        printf("Case #%d: %d\n", Case++, idx);
    }
    return 0;
}
