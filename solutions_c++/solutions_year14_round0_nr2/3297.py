#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <queue>

using namespace std;

typedef long long          ll;
typedef pair <int, int>    ii;
typedef vector <ii>       vii;
typedef vector <int>       vi;
#define INF 1000000000
#define pb push_back
#define mp make_pair

int main() {
    freopen ("inputB.txt","r",stdin);
    freopen ("outputB.txt","w",stdout);
    int k;
    scanf(" %d", &k);
    for (int a = 1; a <= k; a++) {
        long double c, f, x;
        scanf(" %Lf %Lf %Lf", &c, &f, &x);
        int bla = 1;
        long double mini;
        long double last = 0;
        long double rate = 2;
        while (true) {
            long double sem = last + x/rate;
            if (bla == 1) mini = sem;
            bla++;
            last += c/rate;
            rate += f;
            if (mini < sem) {
                break;
            }
            mini = min(mini, sem);
        }
        printf("Case #%d: %.7Lf\n", a, mini);
    }
    return 0;
}
