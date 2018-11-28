//         /\_/\
//   _____/ o o \
//  /~____  =ø= /
// (______)__m_m)

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <stack>
#include <queue>
#include <climits>
#include <limits>
#include <cstring>

#define pb push_back
#define pf push_front
#define all(c) c.begin(), c.end()
#define tr(c, it) \
for(typeof(c.begin()) it = c.begin(); it!=c.end(); ++it)
#define present(container, element) (find(all(container),element) != container.end())
#define present2(c,x) ((c).find(x) != (c).end()) // For maps and set

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const long double PI = 3.141592653589793238462643383;
const ll MOD = 1000000007;
const double EPS = 1e-9; // a==b is abs(a-b)<EPS, a>=b is a>b-EPS, a>b is a>=b+EPS
const int MAX_INT = 2147483647;

using namespace std;

int main()
{
    int T; cin>>T;
    for(int t=1; t<=T; ++t)
    {
        double c,f,x;
        cin>>c>>f>>x;
        vector<double> vec(100000);
        vec[0] = 0.0;
        for(int i=1; i<100000; ++i){
            vec[i] = vec[i-1]+c/(2.0+(i-1)*f);
        }
        double ans = vec[0]+x/(2.0);
        double dummy;
        for(int i=1; i<100000; ++i){
            dummy = vec[i]+x/(2.0+i*f);
            ans = min(ans,dummy);
        }
        cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<ans<<endl;
    }
}