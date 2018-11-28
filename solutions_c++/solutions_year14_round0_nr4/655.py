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

double ma[1000], mb[1000], *mx, *my;
int n;
char ms[1000];
int cal(){
    int res = 0;
    memset(ms, 1, 1000);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mx[i] > my[j] && ms[j]) {
                ms[j] = 0;
                res++;
                break;
            }
        }
    }
    return res;
}
void main2(){
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> ma[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> mb[i];
    }
    sort(ma, ma + n);
    sort(mb, mb + n);

    mx = ma, my = mb;
    cout << cal() << " ";
    mx = mb, my = ma;
    cout << n - cal() << endl;
}
int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        main2();
    }
    return 0;
}
