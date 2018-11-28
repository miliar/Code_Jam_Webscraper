// Librerías útiles.
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <set>
#include <limits>
// Si hay soporte para esto, se puede usar esta única línea:
// #include <bits/stdc++.h>

// Macros útiles (repetición).
#define REP(n) while((n)--)
#define FOR(i, from, to) for (int i = (from) ; i < (to) ; i++)
#define FORS(i, from, to, step) for (int i = (from) ; i != (to) ; i += (step))
#define FOREACH(obj, it) for (typeof((obj).begin()) it = (obj).begin() ; it != (obj).end() ; it++)
#define FOREACHR(obj, it) for (typeof((obj).rbegin()) it = (obj).rbegin() ; it != (obj).rend() ; it++)

// Macros útiles (contenedores).
#define FILL(obj, val) memset(obj, val, sizeof(obj))
#define SIZE(obj) ((int)(obj.size()))
#define ALL(obj) (obj).begin(), (obj).end()
#define RALL(obj) (obj).rbegin(), (obj).rend()
#define IN(elem, obj) (find(ALL(obj), elem) != (obj).end())

// Macros útiles (miscelaneas).
#define BIT(n, i) ((n)&(1<<(i)))
#define LOWBIT(n) ((n)&((n)^((n)-1)))
#define SYNC ios_base::sync_with_stdio(0); cin.tie(NULL);
#define CONV(from, to) if (true) {stringstream ss; ss << from; ss >> to;}

// Macros útiles (abreviaturas).
#define mp make_pair
#define pb push_back

// Macros útiles (constantes).
#define INF 0x3f3f3f3f
#define EPS 1e-6
#define PI 3.1415926535897932384626

using namespace std;

// Aliases de tipos útiles.
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<string> vs;

typedef map<int, int> mii;
typedef map<string, int> msi;
typedef map<int, vi> miv;

// Funciones útiles.
ull gcd(ull a, ull b){ return b ? gcd(b, a % b) : a; }
ull mcm(ull a, ull b){ return a * b / gcd(a, b); }
ll sq(ll a) { return a*a; }
ll pot(ll a, ull b){ return b ? sq(pot(a, b >> 1))*(b & 1 ? a : 1) : 1; }
ll potMod(ll a, ull b, ull m){ return b ? ((sq(potMod(a, b >> 1, m)) % m)*(b & 1 ? a : 1)) % m : 1; }
ull roofLog2(int n) { ull r = 1; for ( ; r < n ; r <<= 1); return r; }
int dbcmp(double a) { if (fabs(a) < EPS) return 0; else return a > 0 ? 1 : - 1; }

int main() {
    
    int t;
    cin >> t;
    FOR (ca, 1, t+1) {
        cout << "CASE #" << ca << ": ";
        int n;
        cin >> n;
        if (!n)
            cout << "INSOMNIA" << endl;
        else {
            int num, ready = 10, nums[10];
            FILL(nums, 0);
            for (num = n; ready ; num += n) {
                string tmp;
                CONV(num, tmp);
                for (int j = 0 ; j < tmp.size() ; j++) {
                    if (!nums[tmp[j]-'0'])
                        ready--;
                    nums[tmp[j]-'0'] = 1;
                }
            }
            cout << (num - n) << endl;
        }
    }
    
    return 0;
    
}
