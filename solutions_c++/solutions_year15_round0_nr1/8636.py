#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<cstring>
#include<queue>
#include<stack>
#include<map>
#include<deque>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Name "A"
#define mp make_pair
const ld eps=1e-9;
const int maxn=3e3;
const ll inf=1e9+7;



int main()
{
//    freopen(Name,"r",stdin);
//    freopen(Name".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 0;i < T;++i)
    {
        int m;
        cin >> m;
        string s;
        cin >> s;
        int an = 0;
        int st = 0;
        for (int i = 0; i <= m; ++i)
        {
            if (st < i)
            {
                an += (i -st);
                st = i;
            }
            st += s[i] - '0';
        }
        cout <<"Case #" << i + 1<<": " << an << "\n";

    }

    return 0;
}
