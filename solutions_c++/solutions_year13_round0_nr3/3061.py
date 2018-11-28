#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
typedef long long ll;
ll n, t, a, b, p[64]={1l, 4l, 9l, 121l, 484l, 12321l, 14641l, 40804l, 44944l, 1234321l, 4008004l, 102030201l, 104060401l, 121242121l, 123454321l, 125686521l, 400080004l, 404090404ll, 10221412201ll, 12102420121ll, 12345654321ll, 40000800004ll, 1002003002001ll, 1004006004001ll, 1020304030201ll, 1022325232201ll, 1024348434201ll, 1210024200121ll, 1212225222121ll, 1214428244121ll, 1232346432321ll, 1234567654321ll, 4000008000004ll, 4004009004004ll}, psize=34;
int main(){
    scanf("%lld", &t);
    for(ll tc = 1; tc <= t; ++tc){
        scanf("%lld %lld", &a, &b);
        n = upper_bound(p, p+psize, b) - lower_bound(p, p+psize, a);
        printf("Case #%lld: %lld\n", tc, n);
    }
}
