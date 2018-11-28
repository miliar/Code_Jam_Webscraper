#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <queue>
#include <iomanip>
#include <cmath>
#include <map>
#include <cstring>

#define MAX
#define INF
#define MOD
#define MP make_pair
#define AA first
#define BB second
#define IS(X) cout << #X << " = " << X << endl;
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef queue<int> QI;
typedef priority_queue<int> PQI;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    int t,cc = 0;cin >> t;
    while(t--) {
        int n;
        cin >> n;
        bool flag[10];
        memset(flag,false,sizeof flag);
        int cnt = 10;
        int r = 0;
        if(!n) {printf("Case #%d: INSOMNIA\n",++cc);continue;}
        while(cnt) {
            r++;
            int tmp = n * r;
            while(tmp) {
                if(!flag[tmp%10]) {flag[tmp%10] = true; cnt--;}
                tmp /= 10;
            }
        }
        printf("Case #%d: %d\n",++cc,n * r);
    }
    return 0;
}
