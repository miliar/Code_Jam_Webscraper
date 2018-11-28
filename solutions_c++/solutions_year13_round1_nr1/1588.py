#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <sstream>
#include <utility>
#include <cctype>
#include <numeric>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <limits>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <functional>
using namespace std;
#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FOR(n)    for(int i=1;i<(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)

#define out(v) cout<<(v)<<endl
#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back
#define             incontainer(c,x)            ( (c).find(x) != (c).end() )
# define nodo pair <int,int>
#define PI 3.14159265
#define MAX 1000000000LL
#define LMT 1E50LL

int main() {
   freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T;
    cin>>T;
    for(int i=1; i<=T; i++) {
        long long int r,t,black_circles=0;
        cin>>r>>t;
        double radioTemp=r+0.0,areaBase=r*r*PI;
        while(t>0) {
                double div=((radioTemp+1)*(radioTemp+1)*(PI)-areaBase)/PI;
                double intpart;
                double decim=modf (div , &intpart);
            if( ( decim==0 )&& (intpart)<=t) {
                radioTemp+=2;
                areaBase=radioTemp*radioTemp*PI;
                t-=intpart;
                black_circles++;
            } else {
                break;
            }
        }
        cout<< "Case #"<<i<<": "<<black_circles<<endl;
    }

    // printf("time = %.18f\n", (clock() - start) / CLOCKS_PER_SEC);
    return 0;
}
