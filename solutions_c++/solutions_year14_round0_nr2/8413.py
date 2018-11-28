#include<iostream>
#include<algorithm>
#define MAXC 500
#define MAXF 4
#define MAXX 2000
using namespace std;

long double c, f, x;

void solve(int test) {
    int farm=0;
    cin>>c>>f>>x;
    //scanf("%Lf%Lf%Lf", &c, &f, &x);
    long double ans = x/2.0;
    while( ans + (c-x)/(2.0+(long double)farm*f) + x/(2.0 + f*((long double)farm+1) ) < ans ) {
        ans += (c-x)/(2.0+(long double)farm*f) + x/(2.0 + f*((long double)farm+1) );
        ++farm;
    }
    //printf("Case #%d: %.7Lf\n", test, ans);
    cout.precision(7);
    std::cout.setf( ios::fixed, ios::floatfield );
    cout<<"Case #"<<test<<": "<<ans<<"\n";
}

int main() {
    int tests;
    //scanf("%d", &tests);
    cin>>tests;
    for(int t=1; t<=tests; ++t)
        solve(t);
    return 0;
}
