//{ Template
using namespace std;
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
#include<sstream>
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
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS DBL_EPSILON
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}
//}

string toString(int number){ stringstream ss;ss << number; return ss.str(); }


bool palin(int n )
{
   string x = toString(n);
   int len = x.length() ;
   rep(i,len) if(x[i] != x[len-i-1]) return false;
   return true;
}

int call(int a,int b){
    int cnt = 0;
    forab(i,a,b){
        if(palin(i)){
            int tmp = sqrt(i);
            if(tmp*tmp==i){
                if(palin(tmp))
                    cnt++;
            }

        }
    }
    return cnt;
}

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int t;
    cin >> t;
    For(cs,t){
        int a,b;
        cin >> a >> b;
        printf("Case #%d: %d\n",cs,call(a,b));
    }
}

