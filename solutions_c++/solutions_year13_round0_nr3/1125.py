#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}
vector<LL> num;
int isP(LL val)
{
    int i, j, cnt = 0, dig[16];
    while(val)
    {
        dig[++cnt] = val % 10;
        val /= 10;
    }
    for(i = 1, j = cnt; i < j; i++, j--)
        if(dig[i] != dig[j])
            return 0;
    return 1;
}
void init(int maxv)
{
    num.clear();
    for(LL i = 1; i <= maxv; i++)
    {
        if(isP(i) && isP(i * i))
            num.push_back(i * i);
    }
}
int main()
{
    //freopen("C-large-1.in", "r", stdin);
    //freopen("C.out", "w", stdout);
    int t, cas = 1;
    LL l, r;
    init(10000000);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%I64d%I64d", &l, &r);
        int lx = lower_bound(num.begin(), num.end(), l) - num.begin();
        int rx = lower_bound(num.begin(), num.end(), r + 1) - num.begin();
        printf("Case #%d: %d\n", cas++, rx - lx);
    }
    return 0;
}

//int main () {
//  int myints[] = {10,20,30,30,20,10,10,20};
//  std::vector<int> v(myints,myints+8);           // 10 20 30 30 20 10 10 20
//
//  std::sort (v.begin(), v.end());                // 10 10 10 20 20 20 30 30
//
//  std::vector<int>::iterator low,up;
//  low=std::lower_bound (v.begin(), v.end(), 20); //          ^
//  up= std::upper_bound (v.begin(), v.end(), 20); //                   ^
//
//  std::cout << "lower_bound at position " << (low- v.begin()) << '\n';
//  std::cout << "upper_bound at position " << (up - v.begin()) << '\n';
//
//  return 0;
//}
