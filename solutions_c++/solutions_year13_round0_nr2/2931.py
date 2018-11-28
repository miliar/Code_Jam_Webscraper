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

// MAIN CODE
int main () {
    input("B-large.in");
    OUTPUT;
    int a, b, arr[200][200], t;
    int potong[200][200], kasus = 0;
    bool bisa;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        for(i=0;i<=110;i++) {
            for(j=0;j<=110;j++) {
                potong[i][j] = 100;
            }
        }
        REP(i, 1, a+1) {
            REP(j, 1, b+1) {
                cin >> arr[i][j];
            }
        }
        for(i=1;i<=100;i++) {
            // CEK BARIS DULU
            for(j=1;j<=a;j++) {
                bisa = true;
                for(k=1;k<=b;k++) {
                    if (arr[j][k] > i)
                        bisa = false;
                }
                if (bisa) {
                    for(k=1;k<=b;k++) {
                        if (potong[j][k] > i)
                            potong[j][k] = i;
                    }
                }
            }
            
            // CEK KOLOM
            for(j=1;j<=b;j++) {
                bisa = true;
                for(k=1;k<=a;k++) {
                    if (arr[k][j] > i)
                        bisa = false;
                }
                if (bisa) {
                    for(k=1;k<=a;k++) {
                        if (potong[k][j] > i)
                            potong[k][j] = i;
                    }
                }
            }
        }
        bisa = true;
        for(i=1;i<=a;i++) {
            for(j=1;j<=b;j++) {
                if (potong[i][j] != arr[i][j])
                    bisa = false;
            }
        }
        cout << "Case #" << ++kasus << ": ";
        if (bisa) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}

// VINCENTIUS MADYA
// DARKSTALKER
// LANGUAGE : C++
