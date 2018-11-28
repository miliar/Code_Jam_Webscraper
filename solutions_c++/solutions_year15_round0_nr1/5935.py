#include <iostream>
#include <string.h>
#include <stdio.h>
#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <algorithm>
#include <map>
#include <streambuf>
#include <sstream>
#include <queue>
#include <iomanip>
#define ll long long
#define INF 1e9
#define PI acos(-1.0)
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
int T;
cin >> T;
int tst = 1;
while(T--)
{

    int n;
    cin >> n;
    string s;
    cin >> s;
    int a[n+1];
    for(int i = 0; i <= n ; i++) a[i] = s[i] - '0';
    int ans = 0;
    int cur = a[0];
    for(int i = 1; i <= n; i++) {
        if(i > cur) {
            ans += i - cur;
            cur += i - cur;
        }
        cur += a[i];
    }
    printf("Case #%d: %d\n",tst++,ans);
}
return 0;
}

