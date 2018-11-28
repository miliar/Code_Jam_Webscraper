#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;
typedef long long LL;
#define N 10005
int ca;
int n , S;
multiset<int> h;

void work() {
    printf("Case #%d: " , ++ ca);
    int i , x , res = 0;
    scanf("%d%d",&n,&S);
    h.clear();
    for (i = 1 ; i <= n ; ++ i) {
        scanf("%d",&x);
        h.insert(x);
    }
    while (!h.empty()) {
        multiset<int>::iterator it =  -- h.end();
        int x = *it ;h.erase(it); ++ res;
        it = h.upper_bound(S - x);
        if (it == h.begin()) continue;
        -- it; x = *it;
        h.erase(it);
    }
    printf("%d\n" , res);
}

int main()
{
    freopen("~input.txt" , "r" , stdin);
    freopen("~output.txt" , "w" , stdout);
    int _; scanf("%d",&_); while (_ --)
        work();
    return 0;
}
