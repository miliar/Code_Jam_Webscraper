/*
Author: Golam Rahman Tushar
........Aust Cse 27th batch.........
*/

//{ Template

//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>

using namespace std;
//}

//}
//{ Floating-points
#define EPS DBL_EPSILON
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}

#define INF 1<<29
#define ll long long

template <typename T>
std::string to_string(T const& value) {
    stringstream sstr;
    sstr << value;
    return sstr.str();
}
//}

template <class T> T gcd(T a,T b){if(b==0) return a;else return gcd(b,a%b);}
template <class T> T lcm(T a,T b){return (a*b)/gcd(a,b);}
template <class T> T power( T a, T b){if(b==0) return 1; T x=a;for(T i=2;i<=b;i++) a=a*x;return a;}
template <class T> T BigMod(T a,T b,T c){if(a==0) return 0;if(b==0) return 1;if(b%2==0){T x=BigMod(a,b/2,c)%c;return (x*x)%c;}else return  ((a%c)*BigMod(a,b-1,c)%c)%c;}

int main ()
{
        int t, i, j, id, cnt1, cnt2, n, Case = 1;
        double p1[11], p2[11];
        cin>>t;
        freopen ("o.txt","w",stdout);
        while(t--)
        {
                cin>>n;
                for(i=0;i<n;i++) cin>>p1[i];
                for(i=0;i<n;i++) cin>>p2[i];

                sort(p1, p1+n);
                sort(p2, p2+n);

                id = cnt1 = 0;
                for(i=0;i<n;i++)
                {
                        if(p1[i]>p2[id]) {
                                cnt1++;
                                id++;
                        }
                }

                id = cnt2 = 0;
                for(i=0;i<n;i++)
                {
                        if(p2[i]>p1[id]) {
                                cnt2++;
                                id++;
                        }
                }

                printf("Case #%d: %d %d\n",Case++,cnt1,n-cnt2);
        }
        return 0;
}
