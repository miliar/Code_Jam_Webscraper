#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <vector>
using namespace std;

vector<long long> zz;

void prepare()
{
    zz.clear();
    zz.push_back(1ll);
    zz.push_back(4ll);
    zz.push_back(9ll);
    zz.push_back(121ll);
    zz.push_back(484ll);
    zz.push_back(10201ll);
    zz.push_back(12321ll);
    zz.push_back(14641ll);
    zz.push_back(40804ll);
    zz.push_back(44944ll);
    zz.push_back(1002001ll);
    zz.push_back(1234321ll);
    zz.push_back(4008004ll);
    zz.push_back(100020001ll);
    zz.push_back(102030201ll);
    zz.push_back(104060401ll);
    zz.push_back(121242121ll);
    zz.push_back(123454321ll);
    zz.push_back(125686521ll);
    zz.push_back(400080004ll);
    zz.push_back(404090404ll);
    zz.push_back(10000200001ll);
    zz.push_back(10221412201ll);
    zz.push_back(12102420121ll);
    zz.push_back(12345654321ll);
    zz.push_back(40000800004ll);
    zz.push_back(1000002000001ll);
    zz.push_back(1002003002001ll);
    zz.push_back(1004006004001ll);
    zz.push_back(1020304030201ll);
    zz.push_back(1022325232201ll);
    zz.push_back(1024348434201ll);
    zz.push_back(1210024200121ll);
    zz.push_back(1212225222121ll);
    zz.push_back(1214428244121ll);
    zz.push_back(1232346432321ll);
    zz.push_back(1234567654321ll);
    zz.push_back(4000008000004ll);
    zz.push_back(4004009004004ll);
}

int run;

void solve()
{
    long long A, B;
    cin >> A >> B;
    int res = 0;
    for (int i = 0; i < zz.size(); i++)
        if (A <= zz[i] && zz[i] <= B) res++;
    printf("Case #%d: %d\n", run, res);
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    prepare();
    int test;
    scanf("%d", &test);
    for (run = 1; run <= test; run++) solve();
    return 0;
}
