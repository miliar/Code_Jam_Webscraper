#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<set>
#include<deque>
#include<cmath>

#define FOR(i,j,k,l) for(((i)=(j));((i)<(k));((i)+=(l)))
#define REP(i,n) for((i)=0;(i)<(n);(i)++)
//#define min(a,b) ((a<b)?(a):(b))
//#define max(a,b) ((a>b)?(a):(b))
typedef long long int ll;
typedef long double ld;

using namespace std;
// 1ml=> pi cm2 
//first => r , t=total mls
int main() {
    int nin, inum;
    int x, y, z, i, j, k, n;
    cin >> nin;
    FOR(inum, 0, nin, 1) {
        //each test case
        ld x;ld r,t;
        cin>>r>>t;
        x=sqrtl((r*r*4.0 -4.0*r+1.0+8.0*t));
        x/=(long double)4.0;
        x+=((ld) 1-2*r)/((ld)4.0);
        x=floorl(x);
        cout<<"Case #"<<inum+1<<": ";printf("%.0Lf\n",x);
    }

    return 0;
}
