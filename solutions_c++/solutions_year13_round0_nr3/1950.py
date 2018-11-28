#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

#define pb push_back

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    unsigned long long int a,b;
    int w;
    vector <unsigned long long int> v;
    v.pb(1); v.pb(4); v.pb(9); v.pb(121); v.pb(484); v.pb(10201); v.pb(12321); v.pb(14641); v.pb(40804); v.pb(44944); v.pb(1002001); v.pb(1234321); v.pb(4008004); v.pb(100020001); v.pb(102030201); v.pb(104060401); v.pb(121242121); v.pb(123454321); v.pb(125686521); v.pb(400080004); v.pb(404090404); v.pb(10000200001); v.pb(10221412201); v.pb(12102420121); v.pb(12345654321); v.pb(40000800004); v.pb(1000002000001); v.pb(1002003002001); v.pb(1004006004001); v.pb(1020304030201); v.pb(1022325232201); v.pb(1024348434201); v.pb(1210024200121); v.pb(1212225222121); v.pb(1214428244121); v.pb(1232346432321); v.pb(1234567654321); v.pb(4000008000004); v.pb(4004009004004);
    
    for (int i=0; i<t; ++i)
    {
        w=0;
        scanf("%llu %llu", &a, &b);
        for (int j=0; j<v.size(); ++j)
        {
            if (v[j] >= a && v[j] <= b) ++w;
        }
        printf("Case #%d: %d\n", i+1, w);
    }



	return 0;
}