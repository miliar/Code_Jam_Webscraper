#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sc(x) scanf("%d",&x)

int main(void){
    #ifdef ccsnoopy
        freopen("D:/Code/A-small-attempt0.in","r",stdin);
        freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);
    #endif
    //to compile: g++ -o foo filename.cpp -lm -Dccsnoopy for debug.
    int tc;
    int dummy;
    int num;
    int rownum;
    int casecounter = 1;
    sc(tc);
    map<int,int> mapper;
    TC(){
        mapper.clear();
        sc(rownum);rownum--;
        FOR(i,4){
            if(rownum == i){
                FOR(j,4){
                    sc(num);
                    mapper[num]++;
                }
            }else FOR(j,4)sc(dummy);
        }
        sc(rownum);rownum--;
        int remember; int total;
        total = 0;
        FOR(i,4){
            if(rownum == i){
                FOR(j,4){
                    sc(num);
                    if(mapper.find(num)!=mapper.end()){
                        total++;
                        remember = num;
                    }
                }
            }else FOR(j,4)sc(dummy);
        }

        printf("Case #%d: ",casecounter++);
        if(total == 1)printf("%d\n",remember);
        else if(total == 0)printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }

    return 0;
}



