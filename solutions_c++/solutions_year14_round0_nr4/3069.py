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
        int N; cin>>N;
        vector<double> naomi(N);
        vector<double> ken(N);
        for(int i=0; i<N; ++i) cin>>naomi[i];
        for(int i=0; i<N; ++i) cin>>ken[i];
        sort(all(naomi));
        sort(all(ken));
        int warScore = N;
        int i=0, j=0;
        while(i<N && j<N){
            if(ken[j]>naomi[i]){
                ++i;
                ++j;
                --warScore;
            }
            else{
                ++j;
            }
        }
        int deceitfulWarScore = 0;
        i = N-1; j = N-1;
        int ii = 0;
        while(j>=0 && i>=ii){
            if(naomi[i]>ken[j]){
                ++deceitfulWarScore;
                --i;
                --j;
            }
            else{
                ++ii;
                --j;
            }
        }
        cout<<"Case #"<<t<<": "<<deceitfulWarScore<<" "<<warScore<<endl;
    }
}