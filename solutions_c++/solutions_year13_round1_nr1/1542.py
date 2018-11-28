#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<iostream>
#include<deque>

#define inf 1000000000

using namespace std;

int main()
{
long long t, r, c, res;
scanf("%lld", &c);
for (int i=1; i<=c; i++){
    scanf("%lld%lld", &r, &t);
    res = 0;
    while(2*r+1<=t){
        t -= 2*r+1;
        r += 2;
        res += 1;
    }
    printf("Case #%lld: %lld\n", i, res);
}
return 0;
}
