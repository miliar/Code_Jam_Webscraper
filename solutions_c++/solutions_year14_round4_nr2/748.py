#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

int n;

pii mas[1005];

pii good[1005];
pii start[1005];

//int res = 1e9;
//
//bool testit()
//{
//    bool less = false;
//    for(int i = 0; i+1 < n; ++i)
//        if(mas[i].second > mas[i+1].second)
//            less = true;
//        else
//            if(less)
//                return false;
//    return true;
//}
//
//int powper()
//{
//    int answ = 0;
//    for(int i = 0; i < n; ++i)
//        for(int j = 0; j < i; ++j)
//            if(mas[j].first > mas[i].first)
//                ++answ;
//    return answ;
//}

void test(int T)
{
    cin>>n;
//    res = 1e9;
    for(int i=0; i<n; ++i)
    {
        cin>>mas[i].second;
        mas[i].first = i;
        good[i] = pii(mas[i].second, mas[i].first);
        start[i] = mas[i];
    }
    sort(good, good + n);
    int mres = 0;
    for(int i=0; i<n; ++i)
    {
        int curpos = start[good[i].second].first;
        if(curpos < n - 1 - i - curpos)
        {
            mres += curpos;
        }
        else
        {
            mres += n - 1 - i - curpos;
        }
        for(int j = good[i].second + 1; j < n; ++j)
            --start[j].first;
    }
//    do
//    {
//        if(testit())
//            res = min(res, powper());
//    }while(next_permutation(mas, mas+n));
//    if(res != mres)
//        printf("Case #%d: %d %d\n", T, res, mres);
    printf("Case #%d: %d\n", T, mres);
}

int main(int argc, const char * argv[])
{
    
    freopen("/Users/olpet/Downloads/GCJ/b.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}