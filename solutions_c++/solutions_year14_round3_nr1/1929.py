#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

int minv;
void cal(int gen, int a, int b){
    if (gen > 40) {
        minv = 50;
        return ;
    }
    if (a >= b) {
        minv = gen;
        return ;
    } else {
        b /= 2;
        cal(gen + 1, a, b);
    }
}
void main2()
{
    i64 a, b;
    char c;
    cin >> a >> c >> b;
    minv = 50;
    i64 r = sqrt(max(a, b)) + 1;
    for (int i = 3; i <= r; i += 2) {
        if (a % i == 0 && b % i == 0) {
            a /= i;
            b /= i;
            i -= 2;
        }
    }
    i64 bb = b;
    if (bb % 2 != 0) {
        minv = 50;
    } else  {
        while (bb != 1 && bb % 2 == 0) {
            bb /= 2;
        }
        if (bb != 1) {
            minv = 50;
        } else {
            cal(0, a, b);
        }
    }
    if (minv >= 50) {
        cout << "impossible" << endl;
    } else {
        cout << minv << endl;
    }
}
int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        main2();
    }
    return 0;
}
