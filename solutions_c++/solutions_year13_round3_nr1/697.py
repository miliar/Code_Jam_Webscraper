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

string vol = "aeiou";
bool isvol(char c)
{
    for (int i = 0; i < vol.size(); i++) {
        if (vol[i] == c) {
            return true;
        }
    }
    return false;
}
int cns[1000001];
void main2()
{
    for (int i = 0; i < 1000001; i++) {
        cns[i] = 0;
    }
    string str; int n;
    cin >> str >> n;
    bool broke = true;
    int cnx = -1;
    int cn = 0;
    i64 res = 0;
    for (int i = 0; i < str.size(); i++) {
        if (!isvol(str[i])) {
            cn++;
        } else {
            broke = true;
            cn = 0;
        }
        if (cn >= n) {
            if (broke) {
                cnx++;
                broke = false;
            }
            int temp = i + 1 - n + 1;
            res += temp;
            cns[cnx] = temp;
            //cout << i << ':' << temp << endl;
        } else {
            if (cnx < 0) {
                continue;
            }
            res += cns[cnx];
        }
    }
    printf("%lld\n", res);
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        main2();
    }
	return 0;
}
