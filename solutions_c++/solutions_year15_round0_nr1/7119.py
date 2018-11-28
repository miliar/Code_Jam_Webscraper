#include <iostream>
#include <sstream>
#include <iomanip>
#include <iosfwd>
#include <algorithm>
#include <iterator>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <numeric>
#include <limits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
using namespace std;

#define MP(a,b) make_pair((a),(b))
#define FOR(i,n) for(int64 i = 0;i <(int64)(n); i++)
#define REP(i,n,m) for(int i =(int)(n);i<(int)(m);i++)
#define MF(a,b) memset((a), (b), sizeof((a)))
typedef long long int64;
typedef pair<int64,int64> ipair;
typedef pair<double,double> dpair;


const int64 INF = numeric_limits<int64>::max();
const int64 MAX_N = 1001;
int64 vals[MAX_N];


int main(int argc, const char * argv[])
{
#ifndef ONLINE_JUDGE
    freopen("/Users/lebinjiang/Project/Xcode/Test/Test/input.txt", "r", stdin);
    freopen("/Users/lebinjiang/Project/Xcode/Test/Test/output.txt", "w", stdout);
#endif
    std::ios::sync_with_stdio(false);
    int T;
    cin>>T;
    FOR(t, T){
        cout<<"Case #"<<t+1<<": ";
        int Smax;
        string bits;
        cin>>Smax>>bits;
        FOR(i, Smax+1)vals[i]=bits[i]-'0';
        int val=0,sum=0;
        if (vals[0]==0) {
            val++;
            sum++;
        }else
            sum+=vals[0];
        REP(i, 1, Smax+1)if(vals[i]){
            if (sum<i) {
                val+=i-sum;
                sum=i;
            }
            sum+=vals[i];
        }
        cout<<val<<endl;
    }
    return 0;
}

