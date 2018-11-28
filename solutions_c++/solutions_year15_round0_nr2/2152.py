
#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))


int main()
{
    freopen("out.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    int t, a[1009];
    int d;
    memset(a, 0, sizeof(a));
    while(cin>>t){
        for(int i = 1; i <= t; i++){
            cin>>d;
            int max_n = 0;
            int res = 1009;
            for(int j = 1; j <= d; j++){
                cin>>a[j];
                if(a[j] > max_n) max_n = a[j];
            }
            for(int j = 1; j <= max_n; j++){
                int sum = 0;
                for(int k = 1; k <= d; k++){
                    sum += (a[k]+j-1)/j - 1;
                }
                sum = sum + j;
                if(res > sum) res = sum;
            }
            cout<<"Case #"<<i<<": "<<res<<endl;
        }
    }
    return 0;
}
