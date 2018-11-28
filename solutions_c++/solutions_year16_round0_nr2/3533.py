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
        string s;
        cin >> s;
        int k = 0;
        for (int i=s.length()-1; i>=0; i--){
            if ((s[i] == '-' && k % 2 == 0) || (s[i] == '+' && k % 2 == 1))
                k++;
        }
        cout << "Case #" << T <<  ": " << k << endl;

    }
    return 0;
}
