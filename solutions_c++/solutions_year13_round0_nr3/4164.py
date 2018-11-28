#include <cstdio>
#include <vector>
#include <map>
#include <cstring>
#include <string>
using namespace std;
bool go(long long a) {
    char s[111];
    sprintf(s,"%lld",a);
    string now = s;
    int l = 0, r= now.length()-1;
    while ( l <= r ) {
        if ( now[l] != now[r] ) return false;
        l++; r--;
    }
    return true;
}
int main() {
    int tc;
    long long limit = 100000000000000ll;
    scanf("%d",&tc);
    vector < long long > v;
    for ( long long i = 1 ; i*i <= limit ; i++ ) {
        if ( go(i) )
            v.push_back(i*i);
    }
    for ( int z= 1 ; z <= tc; z++ ) {
        long long a,b;
        scanf("%lld%lld",&a,&b);
        int ans= 0;
        for ( int i = 0 ; i < v.size() ; i++ ) 
            if ( v[i] >= a && v[i] <= b && go(v[i]) ) 
                ans++;
        printf("Case #%d: %d\n",z,ans);
    }
    return 0;
}
