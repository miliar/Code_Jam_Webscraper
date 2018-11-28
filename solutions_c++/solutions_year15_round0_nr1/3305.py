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
int smax;
string s;

int main()
{
    cin >> T;
    for(int Case = 1; Case <= T; Case++){
        cout << "Case #" << Case << ": ";
        cin >> smax;
        cin >> s;
        int ans = 0, total = s[0] - '0';
        for (int i = 1; i <= smax; i++){
            if (total < i){
                ans += i-total;
                total = i;
            }
            total += s[i] - '0';
        }
        cout << ans << endl;
    }
    return 0;
}
