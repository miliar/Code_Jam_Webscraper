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
    freopen("D-small-attempt1.in","r",stdin);
    freopen("ans.out","w",stdout);
    int t;cin >> t;
    int cc = 0;
    while(t--) {
        printf("Case #%d: ", ++cc);
        int k,c,s;
        cin >> k >> c >> s;
        for(int i = 1;i <= s;i++) printf((i!=s)?"%d " : "%d\n",i);
    }
    return 0;
}
