/*  ^^ ====== ^^
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
#define LOCAL
int main()
{
#ifdef LOCAL
	freopen("C:\\Users\\honm\\Desktop\\in.txt", "r", stdin);
	freopen("C:\\Users\\honm\\Desktop\\out.txt","w",stdout);
#endif
    int t;cin >> t;
    int kase = 1;
    while(t--){
        printf("Case #%d: ",kase++);
        char ch[200];scanf("%s",ch+1);
        int a[200];
        int l = strlen(ch+1);
        for(int i=1;i<=l;i++)if(ch[i]=='-') a[i] = 0;else a[i] = 1;
        int b = ch[1]=='-'?0:1;
        int pos = 2;
        int cnt = 0;
        while(pos <= l){
            if(a[pos]==b)pos++;
            else b^=1,cnt++,pos++;
        }
        if(!b)cnt++;
        cout << cnt << endl;
    }
	return 0;
}
