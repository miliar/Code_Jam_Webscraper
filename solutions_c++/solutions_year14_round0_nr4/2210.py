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
        freopen("D:/Code/D-large.in","r",stdin);
        freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);
    #endif
    //to compile: g++ -o foo filename.cpp -lm -Dccsnoopy for debug.
    int tc;
    double arr[1010];
    double arr2[1010];
    sc(tc);
    int casecounter = 1;
    int deceit, actual;
    int n;
    TC(){
        deceit = actual = 0;
        sc(n);
        FOR(i,n)scanf("%lf",&arr[i]);
        FOR(i,n)scanf("%lf",&arr2[i]);
        sort(arr,arr+n);
        sort(arr2,arr2+n);
        int pointer = 0;
        FOR(i,n){
            while(arr[i]>arr2[pointer]){
                pointer++;
                actual++;
                if(pointer>=n)break;
            }
            pointer++;
            if(pointer >= n)break;
        }
        int pointerstart = 0;
        int pointerend = n-1;
        FOR(i,n){
            if(arr[i]<arr2[pointerstart]){
                pointerend--;
            }else{
                pointerstart++;
                deceit++;
            }
        }
        printf("Case #%d: %d %d\n",casecounter++,deceit,actual);
    }

    return 0;
}



