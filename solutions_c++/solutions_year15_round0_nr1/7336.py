

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-20
#define inf ( 1LL << 30 )
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

# define VI vector<int>
# define VS vector<string>
# define VC vector<char>
# define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define CI(x) scanf(" %d", &x)
#define CL(x) scanf(" %lld", &x)
#define READ(x) freopen(x,"r",stdin)
#define WRITE(x) freopen(x,"w",stdout)

using namespace std;

#define PI 2*acos(0.0)


char s[100005] ;

int main(){
    READ("A-large.in");
    WRITE("A-large.out");

    int t , cas = 0 , Sm , tot = 0 , res = 0 ;
    scanf(" %d", &t) ;
    while(t--){
        scanf(" %d", &Sm) ;
        scanf(" %s", s) ;

        tot = 0 , res = 0 ;

        REP(i , Sm+1){
            if(tot >= i){
                tot += s[i] - '0' ;
            }else{
                res += (i - tot) ;
                tot +=  (i - tot) + (s[i] - '0') ;
            }
        }

        printf("Case #%d: %d\n", ++cas , res) ;
    }

    return 0;
}

