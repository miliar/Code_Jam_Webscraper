// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

int main() {
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;++t) {
        int n,x;
        scanf("%d %d",&n, &x);
        vector<int> f_list(n);
        for(int i=0;i<n;++i) {
            scanf("%d",&f_list[i]);
        }
        sort(ALL(f_list));

        int ans = 0;
        for(int i=0;i<n;++i) {
            if (f_list[i] == -1) continue;
            ++ans;
            for(int j=n-1;j>i;--j) {
                if(f_list[j] != -1 && f_list[i] +f_list[j] <= x) {
                    f_list[j] = -1;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n",t,ans);

    }
    return 0;
}

