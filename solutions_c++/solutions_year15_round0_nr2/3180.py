#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#define abs(x) (((x)>0)?(x):(-x))
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))
using namespace std;
int T;

int main()
{
    cin >> T;
    for(int Case = 1; Case <= T; Case++){
        cout << "Case #" << Case << ": ";
        int d;
        int p[1100];
        int highest = 0, ans = 0;
        cin >> d;
        highest = 0;
        for (int i = 0; i < d; i++) {
            cin >> p[i];
            highest = max(highest, p[i]);
        }
        ans = highest;

        for (int i = 1; i <= highest; i++) {
            int interrupt = 0;
            for (int j = 0; j < d; j++) {
                if (p[j] > i) {
                    interrupt += p[j] / i - 1;
                    if (p[j] % i) {
                        interrupt++;
                    }
                }
            }
            ans = min(ans, interrupt+i);
        }

        cout << ans << endl;
    }
    return 0;
}
