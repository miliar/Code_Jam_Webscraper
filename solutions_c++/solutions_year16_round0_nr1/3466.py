#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define F first
#define S second

const int INF = 1000000000;
const int C = 1000000;
const int mda = 1337 +  14664;

map<int, int> m;

int f[1010];

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #else
        //freopen("encryption.in", "r", stdin);
        //freopen("encryption.out", "w", stdout);
    #endif // LOCAL
    int t, mx=0;
    cin >> t;
    for (int T=1; T<=t; T++){
        int i;
        cin >> i;
        if (i == 0){
            cout << "Case #" << T <<  ": INSOMNIA" << endl;
            continue;
        }
        for (int j=0; j<10; j++)
            f[j] = 0;
        int j = 1, x = i, kl = 10;
        while (kl > 0){
            int y = x;
            while (y > 0){
                if (!f[y % 10])
                    kl--;
                f[y%10] = 1;
                y /= 10;
            }
            //cerr << kl <<  ' '<< x << endl;
            //return 0;
            if (kl == 0) break;
            j++;
            x = i*j;
        }
        cout << "Case #" << T <<  ": " << x << endl;
    }
    return 0;
}
