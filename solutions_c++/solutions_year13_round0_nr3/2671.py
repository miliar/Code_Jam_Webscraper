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

bool pal(int A) {
    string temp;
    while (A > 0) {
        temp.pb((A % 10) + '0');
        A /= 10;
    }
    for(int i=0;i<temp.size()/2;i++) {
        if (temp[i] != temp[temp.size() - i - 1])
            return false;
    }
    return true;
}

// MAIN CODE
int main () {
    input("C-small-attempt0.in");
    OUTPUT;
    int t, a, b, ans, kasus = 0;
    cin >> t;
    while (t--) {
        ans = 0;
        cin >> a >> b;
        for(i=1;i<=1000;i++) {
            if (pal(i) && pal(i*i) && (i*i) >= a && (i*i) <= b) ans++;
        }
        cout << "Case #" << ++kasus << ": " << ans << endl;
    }
    return 0;
}

// VINCENTIUS MADYA
// DARKSTALKER
// LANGUAGE : C++
