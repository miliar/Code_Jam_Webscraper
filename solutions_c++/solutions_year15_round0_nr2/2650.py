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

const int M = 1005;
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

int memo[M][M];

int get_count(int s, int t) {

    int &ans = memo[s][t];

    if(ans != -1) return ans;

    if(s <= t) return 0;

    ans = INF;

    for(int j=1;j<s;++j) ans = min(ans, 1 + get_count(j,t) + get_count(s-j,t));

    return ans;
}

int main() {

    int tc;
    scanf("%d",&tc);
    SET(memo, -1);
    for(int t=1;t<=tc;++t) {

        int dc;
        scanf("%d",&dc);

        vector<int> diners;

        for(int i=0;i<dc;++i) {
            int d;
            scanf("%d", &d);
            diners.push_back(d);
        }

        int ans = INF;
        for(int i = 1; i<= 1000; ++i) {
            int sum = 0;
            for(int j =0; j<SZ(diners);++j) {
                sum += get_count(diners[j], i);
            }

            ans =  min(ans, i + sum);
        }

        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}

