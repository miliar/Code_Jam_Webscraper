#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
typedef long long ll;
int S;
string str;

void work()
{
    int now = 0, ans = 0;
    int i;
    REP(i, S + 1)
    {
        if (now < i) {
            ans += i - now;
            now = i + str[i] - '0';
        }
        else {
            now += str[i] - '0';
        }
    }
    cout << ans << endl;
}

int main()
{
    ios :: sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    int kase = 1;
    while (T --) {
        cin >> S >> str;
        printf("Case #%d: ", kase ++);
        work();
    }
    return 0;
}