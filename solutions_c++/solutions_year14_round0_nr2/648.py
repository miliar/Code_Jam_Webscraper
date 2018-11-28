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


void main2(){
    double C, F, X;
    cin >> C >> F >> X;
    double min_time = X / 2.0;
    double rate = 2;
    double time = 0;
    while (true) {
        time += C / rate;
        if (time + X / (rate + F) >= min_time) {
            break;
        }
        min_time = time + X / (rate + F);
        rate += F;
    }
    printf("%.7lf\n", min_time);
}
int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        main2();
    }
    return 0;
}
