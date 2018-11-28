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


int mx[4];
void main2(){
    int r, x;
    cin >> r;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> x;
            if (r == i + 1) {
                mx[j] = x;
            }
        }
    }
    cin >> r;
    int count = 0, num;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> x;
            if (r == i + 1) {
                for (int k = 0; k < 4; k++) {
                    if (mx[k] == x) {
                        count++;
                        num = x;
                    }
                }
            }
        }
    }
    if (count == 1) {
        cout << num << endl;
    } else if (count != 0) {
        cout << "Bad magician!" << endl;
    } else {
        cout << "Volunteer cheated!" << endl;
    }
}
int main()
{
    int T, t = 1;
    cin >> T;
    while (T--) {
        cout << "Case #" << t++ << ": ";
        main2();
    }
    return 0;
}
