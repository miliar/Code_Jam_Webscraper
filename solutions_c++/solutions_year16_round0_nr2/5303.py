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
    //freopen("B-large.in","r",stdin);
    //freopen("ans.out","w",stdout);
    int t,cc = 0;cin >> t;
    while(t--) {
        char str[105];
        cin >> str;
        str[strlen(str)+1] = '\0';
        str[strlen(str)] = '+';
        int ans = 0;
        for(int i = 0;i < strlen(str)-1;i++) {
            if(str[i] != str[i+1]) ans++;
        }
        printf("Case #%d: %d\n",++cc,ans);
    }
    return 0;
}
