// INCLUDE LIST
#include <cstdio>
#include <bitset>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

// DEFINE LIST
#define REP(_I, _J, _K) for(_I = (_J) ; _I < (_K) ; _I++)
#define input(_A)       freopen(_A, "r", stdin);
#define output(_A)      freopen(_A, "w", stdout);
#define INPUT           input("in.txt");
#define OUTPUT          output("out.txt");
#define CASE_LEFT(_A)   fprintf(stderr, "Cases left: %d\n", R);
#define hold            {fflush(stdin); getchar();}
#define reset(_A, _B)   memset((_A), (_B), sizeof (_A));
#define debug           printf("<<TEST>>\n");
#define eps             1e-11
#define f_cmp(_A, _B)   (fabs((_A) - (_B)) < eps)
#define phi             acos(-1)
#define pb              push_back
#define value(_A)       cout << "Variabel -> " << #_A << " -> " << _A << endl;
#define st              first
#define nd              second

// TYPEDEF LIST
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       LL;

// VAR LIST
int MAX =               1000000;
int MIN =               -1000000;
int INF =               1000000000;
int x4[4] =             {0, 1, 0, -1};
int y4[4] =             {1, 0, -1, 0};
int x8[8] =             {0, 1, 1,  1,  0, -1, -1, -1};
int y8[8] =             {1, 1, 0, -1, -1, -1,  0,  1};
int i, j, k;

LL MAKS(LL A, LL B) {
    if (A > B) return A;
    else return B;
}

// MAIN CODE
int main () {
    input("B-large.in");
    output("out.txt");
    LL t, n, m, kasus = 0ll;
    vector<string> v;
    cin >> t;
    while (t--) {
        v.clear();
        cin >> n >> m;
        LL temp = (1ll << n);
        LL wew = 0ll, indx = temp / 2ll;
        LL po = 0ll;
        LL dua = 2ll;
        while (po + indx <= (m-1ll)) {
            po += indx;
            indx = MAKS(1ll, indx / 2ll);
            wew += dua;
            dua *= 2ll;
        }
        
        LL msk = 0ll;
        indx = temp / 2ll;
        po = 0ll;
        LL tambah = 1ll;
        while (po + tambah <= (m-1ll)) {
            po += tambah;
            tambah *= 2ll;
            msk += indx;
            indx = indx / 2ll;
        }
        
        if (m == temp) {
            wew = m-1ll;
            msk = m-1ll;
        }
        
        cout << "Case #" << ++kasus << ": " << wew << " " << msk << endl;
    }
    return 0;
}

// VINCENTIUS MADYA
// DARKSTALKER
// LANGUAGE : C++
